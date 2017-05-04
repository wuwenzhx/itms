from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth, get_project_object, check_name, check_name_by_id, get_object, check_owner_runner


class FeatureComponentList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        component_list = Component.objects.filter(project__name=project)
        serializer = FeatureComponentSerializer(component_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FeatureComponentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        component_name = serializer.data['name']
        if not check_name(Component, component_name, project):
            return Response({'detail': unicode("Found same name componet, "
                                               "please check your componet name.")},
                            status=status.HTTP_409_CONFLICT)

        new_component = Component.objects.create(
            name=component_name,
            project=get_project_object(project)
        )

        new_serializer = FeatureComponentSerializer(new_component)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class FeatureComponentDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        component_obj = get_object(Component, project, pk)
        serializer = FeatureComponentSerializer(component_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FeatureComponentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        component_name = serializer.data['name']
        if not check_name_by_id(Component, component_name, project, pk):
            return Response({'detail': unicode("Found same name component, "
                                               "please check your component name.")},
                            status=status.HTTP_409_CONFLICT)

        component_obj = get_object(Component, project, pk)
        component_obj.name = component_name
        component_obj.save()

        new_serializer = FeatureComponentSerializer(component_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        component_obj = get_object(Component, project, pk)
        component_obj.feature_set.clear()
        component_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FeatureList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        fea_list = Feature.objects.filter(project__name=project)
        serializer = FeatureSerializer(fea_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FeatureSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            fea_name = serializer.data['name']
            fea_owner = serializer.data['owner']
            fea_component = serializer.data['component']
            fea_requirement = serializer.data['requirement']
            fea_description = serializer.data['description']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_name(Feature, fea_name, project):
            return Response({'detail': unicode("Found same name feature, "
                                               "please check your feature name.")},
                            status=status.HTTP_409_CONFLICT)

        if not check_owner_runner(request.user, fea_owner):
            return Response({'detail': unicode("The owner should be current user - {0}".format(request.user))},
                            status=status.HTTP_400_BAD_REQUEST)

        new_fea = Feature.objects.create(
            name=fea_name,
            owner=fea_owner,
            component_id=fea_component,
            requirement_id=fea_requirement,
            description=fea_description,
            project=get_project_object(project)
        )

        new_serializer = FeatureSerializer(new_fea)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class FeatureDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        fea_obj = get_object(Feature, project, pk)
        serializer = FeatureSerializer(fea_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = FeatureSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            fea_name = serializer.data['name']
            fea_owner = serializer.data['owner']
            fea_component = serializer.data['component']
            fea_requirement = serializer.data['requirement']
            fea_description = serializer.data['description']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_name_by_id(Feature, fea_name, project, pk):
            return Response({'detail': unicode("Found same name feature, "
                                               "please check your feature name.")},
                            status=status.HTTP_409_CONFLICT)

        fea_obj = get_object(Feature, project, pk)

        if not check_owner_runner(fea_obj.owner, fea_owner):
            return Response({'detail': unicode("The owner can not be changed.")},
                            status=status.HTTP_400_BAD_REQUEST)
        fea_obj.name = fea_name
        fea_obj.owner = fea_owner
        fea_obj.component_id = fea_component
        fea_obj.requirement_id = fea_requirement
        fea_obj.description = fea_description
        fea_obj.save()

        new_serializer = FeatureSerializer(fea_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        fea_obj = get_object(Feature, project, pk)
        fea_obj.testcase_set.clear()
        fea_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
