from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object, check_name, check_name_by_id, get_object, \
                  check_owner_runner


class TestexecutionOsList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        os_list = OS.objects.filter(project__name=project)
        serializer = TestexecutionOsSerializer(os_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestexecutionOsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        os_name = serializer.data['name']
        if not check_name(OS, os_name, project):
            return Response({'detail': unicode("Found same name OS, please check your OS name.")},
                            status=status.HTTP_409_CONFLICT)

        new_os = OS.objects.create(name=os_name, project=get_project_object(project))
        new_os.save()
        new_serializer = TestexecutionOsSerializer(new_os)

        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestexecutionOsDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        os_obj = get_object(OS, project, pk)
        serializer = TestexecutionOsSerializer(os_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestexecutionOsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        os_name = serializer.data['name']
        if not check_name_by_id(OS, os_name, project, pk):
            return Response({'detail': unicode("Found same name os, please check your os name.")},
                            status=status.HTTP_409_CONFLICT)

        os_obj = get_object(OS, project, pk)
        os_obj.name = serializer.data['name']
        os_obj.save()

        new_serializer = TestexecutionOsSerializer(os_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        os_obj = get_object(OS, project, pk)
        os_obj.testexecution_set.clear()
        os_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestexecutionPlatformList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        platform_list = Platform.objects.filter(project__name=project)
        serializer = TestexecutionPlatformSerializer(platform_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestexecutionPlatformSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        platform_name = serializer.data['name']
        if not check_name(Platform, platform_name, project):
            return Response({'detail': unicode("Found same name platform, please check your platform name.")},
                            status=status.HTTP_409_CONFLICT)

        new_platform = Platform.objects.create(name=platform_name, project=get_project_object(project))
        new_platform.save()
        new_serializer = TestexecutionPlatformSerializer(new_platform)

        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestexecutionPlatformDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        platform_obj = get_object(Platform, project, pk)
        serializer = TestexecutionPlatformSerializer(platform_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestexecutionPlatformSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        platform_name = serializer.data['name']
        if not check_name_by_id(Platform, platform_name, project, pk):
            return Response({'detail': unicode("Found same name platform, please check your platform name.")},
                            status=status.HTTP_409_CONFLICT)

        platform_obj = get_object(Platform, project, pk)
        platform_obj.name = serializer.data['name']
        platform_obj.save()

        new_serializer = TestexecutionPlatformSerializer(platform_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        platform_obj = get_object(Platform, project, pk)
        platform_obj.testexecution_set.clear()
        platform_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestexecutionList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def _check_os(self, os_id, project):
        count = OS.objects.filter(id=os_id, project__name=project).count()
        return True if 1 == count else False

    def _check_platform(self, platform_id, project):
        count = Platform.objects.filter(id=platform_id, project__name=project).count()
        return True if 1 == count else False

    @check_auth_reader
    def get(self, request, project):
        execution_list = TestExecution.objects.filter(project__name=project)
        serializer = TestexecutionSerializer(execution_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        # check post data
        serializer = TestexecutionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # check execution name
        execution_name = serializer.validated_data['name']
        rw = serializer.validated_data['rw']
        io_size = serializer.validated_data['io_size']
        queue_depth = serializer.validated_data['queue_depth']
        environment = serializer.validated_data['environment']
        #if not check_name(TestExecution, execution_name, project):
        #    return Response({'detail': unicode("Found same name execution, "
        #                                       "please check your execution name.")},
        #                    status=status.HTTP_409_CONFLICT)
        # check os and platform
        #os = serializer.validated_data['os']
        #if not self._check_os(os.id, project):
        #    return Response({'detail': unicode("Not found os({}), please check your os id.".format(os.id))},
        #                    status=status.HTTP_400_BAD_REQUEST)
        #platform = serializer.validated_data['platform']
        #if not self._check_platform(platform.id, project):
        #    return Response({'detail': unicode("Not found platform({}), please check your platform id.".format(platform.id))},
        #                    status=status.HTTP_400_BAD_REQUEST)

        testplan = serializer.validated_data.get('testplan')
        #if testplan.category and 'undated' == testplan.category.name:
        #    count = TestExecution.objects.filter(testplan=testplan).count()
        #    if count > 0:
        #        return Response('execution already exist(This is undated test plan, '
        #                        'just only have one execution).',
        #                        status=status.HTTP_400_BAD_REQUEST)

        runner = serializer.validated_data['runner']
        #if not check_owner_runner(request.user, runner):
        #    return Response({'detail': unicode("The runner should be current user - {0}".format(request.user))},
        #                    status=status.HTTP_400_BAD_REQUEST)

        new_execution = TestExecution.objects.create(
            name=execution_name,
            rw=rw,
            io_size=io_size,
            queue_depth=queue_depth,
            testplan=testplan,
            runner=runner,
            environment=environment,
            project=get_project_object(project)
        )

        serializer = TestexecutionSerializer(new_execution)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TestexecutionDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        execution_obj = get_object(TestExecution, project, pk)
        serializer = TestexecutionSerializer(execution_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestexecutionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            name = serializer.validated_data['name']
            runner = serializer.validated_data['runner']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_name_by_id(TestExecution, name, project, pk):
            return Response({'detail': unicode("Found same name testexecution_name, "
                                               "please check your testexecution_name name.")},
                            status=status.HTTP_409_CONFLICT)

        execution_obj = get_object(TestExecution, project, pk)
        if not check_owner_runner(execution_obj.runner, runner):
            return Response({'detail': unicode("The runner can not be changed.")},
                            status=status.HTTP_400_BAD_REQUEST)

        execution_obj.name = name
        execution_obj.runner = runner
        execution_obj.save()

        new_serializer = TestexecutionSerializer(execution_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        execution_obj = get_object(TestExecution, project, pk)
        execution_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
