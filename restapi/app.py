from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object, check_name, check_name_by_id, get_object


class AppList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        app_list = App.objects.filter(project__name=project)
        serializer = AppSerializer(app_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = AppSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        app_name = serializer.data['name']
        if not check_name(App, app_name, project):
            return Response({'detail': unicode("Found same name app, please check your app name.")},
                            status=status.HTTP_409_CONFLICT)

        new_app = App.objects.create(name=app_name, project=get_project_object(project))
        new_app.save()
        new_serializer = AppSerializer(new_app)

        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class AppDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        app_obj = get_object(App, project, pk)
        serializer = AppSerializer(app_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = AppSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        app_name = serializer.data['name']
        if not check_name_by_id(App, app_name, project, pk):
            return Response({'detail': unicode("Found same name app, please check your app name.")},
                            status=status.HTTP_409_CONFLICT)

        app_obj = get_object(App, project, pk)
        app_obj.name = app_name
        app_obj.save()

        new_serializer = AppSerializer(app_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        # Allow delete app when it not used by case,suite,plan,execution
        app_obj = get_object(App, project, pk)
        if app_obj.testcase_set.count() or app_obj.testsuite_set.count() or \
                app_obj.testplan_set.count() or app_obj.testexecution_set.count() or \
                app_obj.perftestcaseresultdetail_set.count():
            return Response({'detail': unicode('This app has been used.')})

        # Related AppAttr will auto delete before delete app.
        AppAttr.objects.filter(app=app_obj, project__name=project).delete()
        app_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AppAttrList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        attr_list = AppAttr.objects.filter(project__name=project)
        serializer = AppAttrSerializer(attr_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = AppAttrSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # if not check_name(AppAttr, serializer.data['name'], project):
        #     return Response({'detail': unicode("Found same name attr, "
        #                                        "please check your attr name.")},
        #                     status=status.HTTP_409_CONFLICT)

        if AppAttr.objects.filter(name=serializer.validated_data['name'],
                                  app=serializer.validated_data['app'],
                                  project=get_project_object(project)).count():
            return Response({'detail': unicode("Found same name attr, "
                                               "please check your attr name.")},
                            status=status.HTTP_409_CONFLICT)

        new_attr = AppAttr.objects.create(
            name=serializer.data['name'],
            app_id=serializer.data['app'],
            project=get_project_object(project)
        )
        new_serializer = AppAttrSerializer(new_attr)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class AppAttrDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        attr_obj = get_object(AppAttr, project, pk)
        serializer = AppAttrSerializer(attr_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = AppAttrSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        attr_name = serializer.data['name']
        attr_list = AppAttr.objects.filter(name=serializer.validated_data['name'],
                                           app=serializer.validated_data['app'],
                                           project=get_project_object(project))

        length = len(attr_list)
        if length > 1 or (length == 1 and attr_list[0].id != pk):
            return Response({'detail': unicode("Found same name attr, please check your attr name.")},
                            status=status.HTTP_409_CONFLICT)

        attr_obj = get_object(AppAttr, project, pk)
        attr_obj.name = attr_name
        attr_obj.save()

        new_serializer = AppAttrSerializer(attr_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        attr_obj = get_object(AppAttr, project, pk)
        app = App.objects.get(id=attr_obj.app_id)
        if app.testcase_set.count() or app.testsuite_set.count() or \
                app.testplan_set.count() or app.testexecution_set.count():
            return Response({'detail': unicode('This app has been used.')})
        else:
            attr_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
