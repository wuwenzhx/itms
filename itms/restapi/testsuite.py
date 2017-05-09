from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object
from utils import check_name, check_name_by_id, get_object


class TestsuiteSubsystemList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        subsystem_list = Subsystem.objects.filter(project__name=project)
        serializer = TestsuiteSubsystemSerializer(subsystem_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestsuiteSubsystemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        subsystem_name = serializer.data['name']
        if not check_name(Subsystem, subsystem_name, project):
            return Response({'detail': unicode("Found same name subsystem, "
                                               "please check your subsystem name.")},
                            status=status.HTTP_409_CONFLICT)

        new_subsystem = Subsystem.objects.create(
            name=subsystem_name,
            project=get_project_object(project)
        )

        new_serializer = TestsuiteSubsystemSerializer(new_subsystem)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestsuiteSubsystemDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        subsystem_obj = get_object(Subsystem, project, pk)
        serializer = TestsuiteSubsystemSerializer(subsystem_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestsuiteSubsystemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        subsystem_name = serializer.data['name']
        if not check_name_by_id(Subsystem, subsystem_name, project, pk):
            return Response({'detail': unicode("Found same name subsystem, "
                                               "please check your subsystem name.")},
                            status=status.HTTP_409_CONFLICT)

        subsystem_obj = get_object(Subsystem, project, pk)
        subsystem_obj.name = subsystem_name
        subsystem_obj.save()

        new_serializer = TestsuiteSubsystemSerializer(subsystem_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        subsystem_obj = get_object(Subsystem, project, pk)
        subsystem_obj.testsuite_set.clear()
        subsystem_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestsuiteList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        suite_list = TestSuite.objects.filter(project__name=project, del_flag=False)
        serializer = TestsuiteSerializer(suite_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestsuiteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            suite_name = serializer.validated_data['name']
            suite_subsystem = serializer.validated_data['subsystem']
            suite_description = serializer.validated_data['description']
            plan_list = serializer.validated_data['testplan']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        perf = serializer.validated_data.get('performance', False)
        app = serializer.validated_data.get('app', None)
        if perf and not app:
                return Response({'detail': unicode("parameter app must provide when performance=True")},
                                status=status.HTTP_400_BAD_REQUEST)
        if not perf and app:
                return Response({'detail': unicode("parameter app can not be set when performance=False")},
                                status=status.HTTP_400_BAD_REQUEST)

        if not check_name(TestSuite, suite_name, project, check_flag=True):
            return Response({'detail': unicode("Found same name testsuite, "
                                               "please check your testsuite name.")},
                            status=status.HTTP_409_CONFLICT)

        for plan in plan_list:
            if plan.performance != perf or plan.app != app:
                return Response({'detail': unicode("plan:{0} not match test suite of "
                                                   "performance type".format(plan.id))},
                                status=status.HTTP_409_CONFLICT)

        new_suite = TestSuite.objects.create(
            name=suite_name,
            subsystem=suite_subsystem,
            performance=perf,
            app=app,
            description=suite_description,
            project=get_project_object(project)
        )
        for plan in plan_list:
            new_suite.testplan.add(plan)

        new_suite.save()
        new_serializer = TestsuiteSerializer(new_suite)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestsuiteDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        suite_obj = get_object(TestSuite, project, pk)
        if suite_obj.del_flag:
            return Response({'detail': unicode("Not found suite({})".format(pk))},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = TestsuiteSerializer(suite_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestsuiteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            suite_name = serializer.validated_data['name']
            suite_subsystem = serializer.validated_data['subsystem']
            suite_description = serializer.validated_data['description']
            plan_list = serializer.validated_data['testplan']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        perf = serializer.validated_data.get('performance', False)
        app = serializer.validated_data.get('app', None)
        if perf and not app:
                return Response({'detail': unicode("parameter app must provide when performance=True")},
                                status=status.HTTP_400_BAD_REQUEST)
        if not perf and app:
                return Response({'detail': unicode("parameter app can not be set when performance=False")},
                                status=status.HTTP_400_BAD_REQUEST)

        if not check_name_by_id(TestSuite, suite_name, project, pk, check_flag=True):
            return Response({'detail': unicode("Found same name testsuite_name, "
                                               "please check your testsuite_name name.")},
                            status=status.HTTP_409_CONFLICT)

        suite_obj = get_object(TestSuite, project, pk)
        if suite_obj.performance != perf or suite_obj.app != app:
            return Response({'detail': unicode("Not allow change performance and app attribute.")},
                            status=status.HTTP_400_BAD_REQUEST)

        suite_obj.name = suite_name
        suite_obj.subsystem = suite_subsystem
        suite_obj.description = suite_description

        validated_plan_list = []
        for plan in plan_list:
            if plan.performance != perf or plan.app != app:
                return Response({'detail': unicode("plan:{0} not match test suite of "
                                                   "performance type".format(plan.id))},
                                status=status.HTTP_409_CONFLICT)
            validated_plan_list.append(plan)

        suite_obj.save()
        suite_obj.testplan.clear()
        for plan in validated_plan_list:
            suite_obj.testplan.add(plan)

        new_serializer = TestsuiteSerializer(suite_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        suite_obj = get_object(TestSuite, project, pk)
        suite_obj.del_flag = True
        suite_obj.testplan.clear()
        suite_obj.testcase_set.clear()
        suite_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
