from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.http import QueryDict
from base_models.models import *
from django.contrib.auth import authenticate, login, logout


class IndexProjectPlugin(CMSPluginBase):
    name = 'index'
    render_template = "index.html"

    def _get_myproject_list(self, group_list, project_list):
        my_project_list = []
        for project in project_list:
            if project.reader_group in group_list or project.writer_group in group_list:
                my_project_list.append(project.name)
        return my_project_list

    def render(self, context, instance, placeholder):
        argpost = QueryDict.dict(context['request'].POST)

        user_login_status = False
        my_project_list = None
        message = ""

        if 'user' in argpost and 'password' in argpost:
            user = authenticate(username=argpost.get('user'), password=argpost.get('password'))

            if user is not None:
                if user.is_active:
                    group_list = user.groups.values_list('name', flat=True)
                    print group_list
                    project_list = Project.objects.all()
                    my_project_list = self._get_myproject_list(group_list, project_list)
                    print '=' * 40
                    print my_project_list
                    print '=' * 40

                    user_login_status = True
                    context['username'] = argpost.get('user')

                    if my_project_list:
                        login(context['request'], user)
                    else:
                        message = 'please access eam.intel.com to get related permissions.'
                else:
                    message = 'The password is valid, but the account has been disabled!~'
            else:
                message = 'The username and password were incorrect.'

        if 'project' in argpost:
            context['request'].session['project'] = argpost.get('project')

        #context['user_login_status'] = user_login_status
        context['user_login_status'] = True
        context['message'] = message
        context['project_list'] = my_project_list
        return context

class LogoutPlugin(CMSPluginBase):
    name = 'logout'
    render_template = "logout.html"

    def render(self, context, instance, placeholder):
        logout(context['request'])
        context['auth_flag'] = False
        return context

plugin_pool.register_plugin(IndexProjectPlugin)
plugin_pool.register_plugin(LogoutPlugin)
