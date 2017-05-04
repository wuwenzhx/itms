from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#the # is i  have changed:
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class ProjectList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request):
        if request.user.is_active:
            project_list = Project.objects.all()
            serializer = ProjectSerializer(project_list, many=True)
            content, auth_status = serializer.data, status.HTTP_200_OK
        else:
            content = {
              'detail': unicode("The password is valid, but the account has been disabled!~"),
            }
            auth_status = status.HTTP_401_UNAUTHORIZED
        return Response(content, status=auth_status)
        #return Response(content)
