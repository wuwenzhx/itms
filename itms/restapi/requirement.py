from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import Http404
from utils import check_auth, get_project_object, check_name, check_name_by_id, get_object, check_owner_runner


class RequirementTypeList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        type_list = Type.objects.filter(project__name=project)
        serializer = RequirementTypeSerializer(type_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = RequirementTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        type_name = serializer.data['name']
        if not check_name(Type, type_name, project):
            return Response({'detail': unicode("Found same name type, please check your type name.")},
                            status=status.HTTP_409_CONFLICT)

        new_type = Type.objects.create(name=type_name, project=get_project_object(project))
        new_type.save()
        new_serializer = RequirementTypeSerializer(new_type)

        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class RequirementTypeDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        type_obj = get_object(Type, project, pk)
        serializer = RequirementTypeSerializer(type_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = RequirementTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        type_name = serializer.data['name']
        if not check_name_by_id(Type, type_name, project, pk):
            return Response({'detail': unicode("Found same name type, please check your type name.")},
                            status=status.HTTP_409_CONFLICT)

        type_obj = get_object(Type, project, pk)
        type_obj.name = serializer.data['name']
        type_obj.save()

        new_serializer = RequirementTypeSerializer(type_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        type_obj = get_object(Type, project, pk)
        type_obj.requirement_set.clear()
        type_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RequirementList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, project):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        req_list = Requirement.objects.filter(project__name=project)
        serializer = RequirementSerializer(req_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = RequirementSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            req_name = serializer.data['name']
            req_owner = serializer.data['owner']
            req_type = serializer.data['type']
            req_description = serializer.data['description']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_name(Requirement, req_name, project):
            return Response({'detail': unicode("Found same name requirement, "
                                               "please check your requirement name.")},
                            status=status.HTTP_409_CONFLICT)

        if not check_owner_runner(request.user, req_owner):
            return Response({'detail': unicode("The owner should be current user - {0}".format(request.user))},
                            status=status.HTTP_400_BAD_REQUEST)

        new_req = Requirement.objects.create(
            name=req_name,
            owner=req_owner,
            type_id=req_type,
            description=req_description,
            project=get_project_object(project)
        )

        new_serializer = RequirementSerializer(new_req)
        return Response(new_serializer.data, status=status.HTTP_201_CREATED)


class RequirementDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def _get_req(self, project, pk):
        try:
            req_obj = Requirement.objects.get(id=pk, project__name=project)
        except Requirement.DoesNotExist:
            raise Http404
        return req_obj

    def get(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'reader')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        req_obj = self._get_req(project, pk)
        serializer = RequirementSerializer(req_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        serializer = RequirementSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            req_name = serializer.data['name']
            req_owner = serializer.data['owner']
            req_type = serializer.data['type']
            req_description = serializer.data['description']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_name_by_id(Requirement, req_name, project, pk):
            return Response({'detail': unicode("Found same name requirement, "
                                               "please check your requirement name.")},
                            status=status.HTTP_409_CONFLICT)

        req_obj = self._get_req(project, pk)

        if not check_owner_runner(req_obj.owner, req_owner):
            return Response({'detail': unicode("The owner can not be changed.")},
                            status=status.HTTP_400_BAD_REQUEST)

        req_obj.name = req_name
        req_obj.owner = req_owner
        req_obj.type_id = req_type
        req_obj.description = req_description
        req_obj.save()

        new_serializer = RequirementSerializer(req_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, project, pk):
        auth_status, message = check_auth(request.user, project, 'writer')
        if not auth_status:
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

        req_obj = self._get_req(project, pk)
        req_obj.feature_set.clear()
        req_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
