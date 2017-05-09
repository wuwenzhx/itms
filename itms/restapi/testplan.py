from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object
from utils import check_name, check_name_by_id, get_object, check_owner_runner


class TestplanCategoryList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        category_list = Category.objects.filter(project__name=project)
        serializer = TestPlanCategorySerializer(category_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestPlanCategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        category_name = serializer.data['name']
        if not check_name(Category, category_name, project):
            return Response({'detail': unicode("Found same name category, "
                                               "please check your category name.")},
                            status=status.HTTP_409_CONFLICT)

        new_category = Category.objects.create(
            name=category_name,
            project=get_project_object(project)
        )

        new_serializer = TestPlanCategorySerializer(new_category)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestplanCategoryDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        category_obj = get_object(Category, project, pk)
        serializer = TestPlanCategorySerializer(category_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestPlanCategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        category_name = serializer.data['name']
        if not check_name_by_id(Category, category_name, project, pk):
            return Response({'detail': unicode("Found same name category, "
                                               "please check your category name.")},
                            status=status.HTTP_409_CONFLICT)

        category_obj = get_object(Category, project, pk)
        category_obj.name = category_name
        category_obj.save()

        new_serializer = TestPlanCategorySerializer(category_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        category_obj = get_object(Category, project, pk)
        category_obj.testplan_set.clear()
        category_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestplanList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        plan_list = TestPlan.objects.filter(project__name=project, del_flag=False)
        serializer = TestPlanSerializer(plan_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = TestPlanSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            plan_name = serializer.validated_data['name']
            rw = serializer.validated_data['rw']
            io_size = serializer.validated_data['io_size']
            queue_depth = serializer.validated_data['queue_depth']
            owner = serializer.validated_data['owner']
            plan_description = serializer.validated_data['description']
            create_time = serializer.validated_data['create_time']
        except KeyError:
            pass
        #    return Response({'detail': unicode("The lack of required parameters.")},
        #                    status=status.HTTP_400_BAD_REQUEST)

        #perf = serializer.validated_data.get('performance', False)
        #app = serializer.validated_data.get('app', None)
        #if perf and not app:
        #        return Response({'detail': unicode("parameter app must provide when performance=True")},
        #                        status=status.HTTP_400_BAD_REQUEST)
        #if not perf and app:
        #        return Response({'detail': unicode("parameter app can not be set when performance=False")},
        #                        status=status.HTTP_400_BAD_REQUEST)

        #if not check_name(TestPlan, plan_name, project, check_flag=True):
            #return Response({'detail': unicode("Found same name testplan, "
            #                                   "please check your testplan name.")},
            #                status=status.HTTP_409_CONFLICT)

        #if not check_owner_runner(request.user, plan_owner):
        #    return Response({'detail': unicode("The owner should be current user - {0}".format(request.user))},
        #                    status=status.HTTP_400_BAD_REQUEST)

        new_plan = TestPlan.objects.create(
            name=plan_name,
            rw=rw,
            io_size=io_size,
            queue_depth=queue_depth,
            owner=owner,
            #start_time=start_time,
            #end_time=end_time,
            description=plan_description,
            project=get_project_object(project)
        )

        new_serializer = TestPlanSerializer(new_plan)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class TestplanDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        plan_obj = get_object(TestPlan, project, pk)
        if plan_obj.del_flag:
            return Response({'detail': unicode("Not found plan{}".format(pk))},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = TestPlanSerializer(plan_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestPlanSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            plan_name = serializer.validated_data['name']
            plan_category = serializer.validated_data['category']
            plan_owner = serializer.validated_data['owner']
            plan_description = serializer.validated_data['description']
            start_time = serializer.validated_data['start_time']
            end_time = serializer.validated_data['end_time']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        perf = serializer.validated_data.get('performance', False)
        app = serializer.validated_data.get('app', None)

        if not check_name_by_id(TestPlan, plan_name, project, pk, check_flag=True):
            return Response({'detail': unicode("Found same name testplan, "
                                               "please check your testplan name.")},
                            status=status.HTTP_409_CONFLICT)

        plan_obj = get_object(TestPlan, project, pk)
        if plan_obj.performance != perf or plan_obj.app != app:
            return Response({'detail': unicode("Not allow change performance and app attribute.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_owner_runner(plan_obj.owner, plan_owner):
            return Response({'detail': unicode("The owner can not be changed.")},
                            status=status.HTTP_400_BAD_REQUEST)

        plan_obj.name = plan_name
        plan_obj.owner = plan_owner
        plan_obj.category = plan_category
        plan_obj.start_time = start_time
        plan_obj.end_time = end_time
        plan_obj.description = plan_description
        plan_obj.save()

        new_serializer = TestPlanSerializer(plan_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        plan_obj = get_object(TestPlan, project, pk)
        plan_obj.del_flag = True
        plan_obj.testsuite_set.clear()
        plan_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
