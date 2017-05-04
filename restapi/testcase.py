from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object, check_name
from utils import check_name_by_id, get_object


class TestcaseTypeList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        type_list = TestCaseType.objects.filter(project__name=project)
        serializer = TestcaseTypeSerializer(type_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestcaseTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        type_name = serializer.data['name']
        if not check_name(TestCaseType, type_name, project):
            return Response({'detail': unicode("Found same name type, please check your type name.")},
                            status=status.HTTP_409_CONFLICT)

        new_type = TestCaseType.objects.create(
            name=type_name,
            project=get_project_object(project)
        )

        new_serializer = TestcaseTypeSerializer(new_type)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestcaseTypeDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        type_obj = get_object(TestCaseType, project, pk)
        serializer = TestcaseTypeSerializer(type_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestcaseTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        type_name = serializer.data['name']
        if not check_name_by_id(TestCaseType, type_name, project, pk):
            return Response({'detail': unicode("Found same name type, "
                                               "please check your type name.")},
                            status=status.HTTP_409_CONFLICT)

        type_obj = get_object(TestCaseType, project, pk)
        type_obj.name = type_name
        type_obj.save()

        new_serializer = TestcaseTypeSerializer(type_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        type_obj = get_object(TestCaseType, project, pk)
        type_obj.testcase_set.clear()
        type_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestcaseList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        case_list = TestCase.objects.filter(project__name=project, del_flag=False)
        serializer = TestcaseSerializer(case_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestcaseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            case_name = serializer.validated_data['name']
            case_type = serializer.validated_data['type']
            case_description = serializer.validated_data['description']
            case_script_path = serializer.validated_data['script_path']
            case_config_path = serializer.validated_data['config_path']
            case_parameters = serializer.validated_data['parameters']
            case_feature = serializer.validated_data['feature']
            suite_list = serializer.validated_data['testsuite']
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

        if not check_name(TestCase, case_name, project, check_flag=True):
            return Response({'detail': unicode("Found same name testcase, "
                                               "please check your testcase name.")},
                            status=status.HTTP_409_CONFLICT)

        for suite in suite_list:
            if suite.performance != perf or suite.app != app:
                return Response({'detail': unicode("suite:{0} not match test case of "
                                                   "performance type".format(suite.id))},
                                status=status.HTTP_409_CONFLICT)

        new_case = TestCase.objects.create(
            name=case_name,
            type=case_type,
            description=case_description,
            script_path=case_script_path,
            config_path=case_config_path,
            parameters=case_parameters,
            feature=case_feature,
            performance=perf,
            app=app,
            project=get_project_object(project)
        )

        for suite in suite_list:
            new_case.testsuite.add(suite)
        new_case.save()
        new_serializer = TestcaseSerializer(new_case)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestcaseDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        case_obj = get_object(TestCase, project, pk)
        if case_obj.del_flag:
            return Response({'detail': unicode("Not found case({})".format(pk))},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = TestcaseSerializer(case_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestcaseSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            case_name = serializer.validated_data['name']
            case_type = serializer.validated_data['type']
            case_description = serializer.validated_data['description']
            case_script_path = serializer.validated_data['script_path']
            case_config_path = serializer.validated_data['config_path']
            case_parameters = serializer.validated_data['parameters']
            case_feature = serializer.validated_data['feature']
            suite_list = serializer.validated_data['testsuite']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        # app must be set if performance equal true
        perf = serializer.validated_data.get('performance', False)
        app = serializer.validated_data.get('app', None)
        if perf and not app:
                return Response({'detail': unicode("parameter app must provide when performance=True")},
                                status=status.HTTP_400_BAD_REQUEST)
        if not perf and app:
                return Response({'detail': unicode("parameter app can not be set when performance=False")},
                                status=status.HTTP_400_BAD_REQUEST)

        if not check_name_by_id(TestCase, case_name, project, pk, check_flag=True):
            return Response({'detail': unicode("Found same name testcase_name, "
                                               "please check your testcase_name name.")},
                            status=status.HTTP_409_CONFLICT)

        case_obj = get_object(TestCase, project, pk)
        if case_obj.performance != perf or case_obj.app != app:
            return Response({'detail': unicode("Not allow change performance and app attribute.")},
                            status=status.HTTP_400_BAD_REQUEST)

        case_obj.name = case_name
        case_obj.type = case_type
        case_obj.description = case_description
        case_obj.script_path = case_script_path
        case_obj.config_path = case_config_path
        case_obj.parameters = case_parameters
        case_obj.feature = case_feature

        validated_suite_list = []
        for suite in suite_list:
            if suite.performance != perf or suite.app != app:
                return Response({'detail': unicode("suite:{0} not match test case of "
                                                   "performance type".format(suite.id))},
                                status=status.HTTP_409_CONFLICT)
            validated_suite_list.append(suite)

        case_obj.save()
        case_obj.testsuite.clear()
        for suite in validated_suite_list:
            case_obj.testsuite.add(suite)

        new_serializer = TestcaseSerializer(case_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        case_obj = get_object(TestCase, project, pk)
        case_obj.del_flag = True
        case_obj.testsuite.clear()
        case_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)