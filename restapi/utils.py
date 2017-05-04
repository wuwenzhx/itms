from base_models.models import *
import time
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


# This function will be drop, user decorator check_auth_reader & check_auth_writer to replace it.
def check_auth(user, project, check_type):
# if user.is_active:
#     group_list = user.groups.values_list('name', flat=True)
#     my_project = Project.objects.get(name=project)
#
#     if 'reader' == check_type:
#         if my_project.reader_group in group_list or my_project.writer_group in group_list:
#             auth_status, msg = True, ""
#         else:
#             auth_status, msg = False, "You don't have read permission to access {project} project."\
#                 .format(project=project)
#     elif 'writer' == check_type:
#         if my_project.writer_group in group_list:
#             auth_status, msg = True, ""
#         else:
#             auth_status, msg = False, "You don't have write permission to access {project} project."\
#                 .format(project=project)
#     else:
#         auth_status, msg = False, "internal error check_type={check_type}"\
#             .format(check_type=check_type)
#
#     return auth_status, msg
# else:
#     return False, 'Please provide username and password by base authentication.'
    return True, ""


def check_auth_reader(method):
    def _wrapped_method(*args, **kwargs):
#      request = args[1]
#      project = kwargs.get('project')
#      if request.user.is_active:
#          group_list = request.user.groups.values_list('name', flat=True)
#          my_project = Project.objects.get(name=project)
#          if my_project.reader_group in group_list or my_project.writer_group in group_list:
#              return method(*args, **kwargs)
#          else:
#              return Response("You don't have read permission to access {0} project.".format(project),
#                              status=status.HTTP_401_UNAUTHORIZED)
        return method(*args, **kwargs)
    return _wrapped_method


def check_auth_writer(method):
    def _wrapped_method(*args, **kwargs):
#       request = args[1]
#       project = kwargs.get('project')
#       if request.user.is_active:
#           group_list = request.user.groups.values_list('name', flat=True)
#           my_project = Project.objects.get(name=project)
#           if my_project.writer_group in group_list:
#               return method(*args, **kwargs)
#           else:
#               return Response("You don't have write permission to access {project} project.".format(project),
#                               status=status.HTTP_401_UNAUTHORIZED)
        return method(*args, **kwargs)
    return _wrapped_method


def get_project_object(project_name):
    obj = Project.objects.get(name=project_name)
    return obj


def check_name(obj, name, project, check_flag=False):
    if check_flag:
        count = obj.objects.filter(name=name, project__name=project, del_flag=False).count()
    else:
        count = obj.objects.filter(name=name, project__name=project).count()
    return True if not count else False


def check_name_by_id(obj, name, project, pk, check_flag=False):
    if check_flag:
        obj_list = obj.objects.filter(name=name, project__name=project, del_flag=False)
    else:
        obj_list = obj.objects.filter(name=name, project__name=project)
    if not len(obj_list):
        return True
    elif 1 == len(obj_list) and str(obj_list[0].id) == pk:
        return True
    else:
        return False


def check_case_in_suite(testcase, suite_result):
    if suite_result.testsuite in testcase.testsuite.all():
        return None
    else:
        return 'test case(%s) not in test suite result(%s)' % (testcase.id, suite_result.id)


def check_app_attr(key, app, project):
    app_attr_list = AppAttr.objects.filter(app=app, project__name=project)
    return True if key in app_attr_list else False


def get_object(obj, project, pk):
    if not pk:
        return None
    try:
        obj = obj.objects.get(id=pk, project__name=project)
    except:
        raise Http404
    return obj


def check_owner_runner(user, input_user):
    return True if str(user) == str(input_user) else False
