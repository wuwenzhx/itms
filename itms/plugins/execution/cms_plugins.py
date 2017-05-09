from __future__ import division
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.http import QueryDict
from plugins.execution.models import *
from base_models.models import *
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from utils.decorators import check_login_required_flag
from interact import get_itec_info, post_env_setting, process_data, process_worker_detail
import json
import os
from django import forms

CURRENT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
PROJECT_PATH = os.path.split(CURRENT_PATH)[0]
MEDIA_PATH = os.path.join(PROJECT_PATH, "media")


class FileForm(forms.Form):
    patch = forms.FileField()


def paginator(argpost, data):
    if data is None:
        return [], []
    after_range_num = 5
    before_range_num = 4

    entry_num = int(argpost.get('entry_num', 5))
    my_paginator = Paginator(data, entry_num)
    para = argpost.get('page', 1)
    page = 1
    if para:
        page = int(para)

    try:
        page_list = my_paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        page_list = my_paginator.page(my_paginator.num_pages)

    if page >= after_range_num:
        page_range = my_paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = my_paginator.page_range[0:page + before_range_num]

    return page_list, page_range, entry_num


class ExePlugin(CMSPluginBase):
    name = 'exe_plugin'
    model = ExeInfo
    render_template = 'exe_plugin.html'
    fields = ('title', 'size', 'path')

    @staticmethod
    def _get_testplan_filter_data(para, project, context):
        filter_obj = {'del_flag': False, 'project_id': project}
        context['testplan_list'] = TestPlan.objects.filter(**filter_obj)
        context['category_list'] = Category.objects.filter(project_id=project)
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _search_plan(para, project, context):
        category_name = para.get('category_name', None)
        is_perf = para.get('is_perf', None)
        plan_name = para.get('plan_name', None)

        filter_obj = {'del_flag': False, 'project_id': project}
        if category_name:
            filter_obj['category__name'] = category_name
        if is_perf:
            filter_obj['performance'] = is_perf == str(True)
        if plan_name:
            filter_obj['name__icontains'] = plan_name
        context['testplan_list'] = TestPlan.objects.filter(**filter_obj)
        context['status'] = 'SUCCESS'
        context['message'] = ''

        return context

    @staticmethod
    def _add_exe(para, project, context):
        count = Environment.objects.filter(
            name=para['name'],
            project_id=project).count()

        if count:
            status, message = 'ERROR', 'This execution already exists.'
        else:
            Environment.objects.create(
                name=para['name'],
                schedule=para.get('schedule', None),
                runtime=para.get('runtime', None),
                commit_id=para.get('commit_id', None),
                package=para.get('package', None),
                patch=para.get('patch', None),
                testplan_id=para['testplan'],
                is_invalid=para['is_invalid'] == str(True),
                worker=para['worker'],
                owner=para['owner'],
                itec_id=para['itec_id'],
                env_type_id=para['env_type_id'],
                git_repo=para.get('gitrepo', None),
                project_id=project
            )

            exe = Environment.objects.get(
                name=para['name'],
                project_id=project
            )

            # save config
            Configuration.objects.create(
                project_id=project,
                env_id=exe.id,
                os=para.get('os', None),
                kernel=para.get('kernel', None),
                gcc=para.get('gcc', None),
                target=para.get('target', None),
                nic=para.get('nic', None),
                test_type=para.get('test_type', None),
                driver=para.get('driver', None),
                platform=para.get('platform', None)
            )
            status, message = 'SUCCESS', ''

            # regular execution, deliver para to itec server
            if int(exe.env_type.id) is 1:
                config = Configuration.objects.get(env_id=exe.id)
                payload = {
                    'name': exe.name,
                    'testplan': exe.testplan,
                    'itec': exe.itec.ip,
                    'worker': exe.worker,
                    'owner': exe.owner,
                    'os': config.os,
                    'kernel': config.kernel,
                    'gcc': config.gcc,
                    'target': config.target,
                    'nic': config.nic,
                    'test_type': config.test_type,
                    'driver': config.driver,
                    'platform': config.platform,
                    'env_type': exe.env_type.name,
                    'schedule': exe.schedule,
                    'start_time': exe.runtime,
                    'git_repo': exe.git_repo,
                    'user_email': para['user_email']
                }
                post_env_setting(payload)
            context['exe_id'] = exe.id

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_exe(para, project, context):
        count = Environment.objects.filter(
            name=para['name'],
            project_id=project).count()
        origin_patch = None
        exe = None
        patch = para.get('patch', None)

        if count == 1:
            exe = Environment.objects.get(
                name=para['name'],
                project_id=project
            )
            origin_patch = exe.patch
            if exe.id == int(para['id']):
                # modify without name
                exe.worker = para.get('worker', None)
                exe.package = para.get('package', None)
                exe.testplan_id = para['testplan']
                exe.itec_id = para['itec_id']
                exe.git_repo = para.get('gitrepo', None)
                if patch:
                    exe.patch = para.get('patch', None)
                exe.save()
                status, message = 'SUCCESS', ''
            else:
                status, message = 'ERROR', 'This environment already exists.'
        elif count == 0:
            exe = Environment.objects.get(id=para['id'])
            origin_patch = exe.patch
            exe.name = para['name']
            exe.worker = para.get('worker', None)
            exe.package = para.get('package', None)
            exe.testplan_id = para['testplan']
            exe.itec_id = para['itec_id']
            exe.git_repo = para.get('gitrepo', None)
            if patch:
                exe.patch = para.get('patch', None)
            exe.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        # save configuration
        if status == 'SUCCESS':
            config = Configuration.objects.get(env_id=exe.id)
            config.os = para.get('os', None)
            config.nic = para.get('nic', None)
            config.test_type = para.get('test_type', None)
            config.kernel = para.get('kernel', None)
            config.gcc = para.get('gcc', None)
            config.target = para.get('target', None)
            config.driver = para.get('driver', None)
            config.platform = para.get('platform', None)
            config.save()

        # if modify patch, delete original patch
        if patch:
            file_name = MEDIA_PATH + "/" + str(origin_patch)
            count = Environment.objects.filter(project_id=project, patch=file_name).count()
            if count == 0:
                if os.path.exists(file_name):
                    os.remove(file_name)

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_exe(para, project, context):
        try:
            exe = Environment.objects.get(id=para['id'])
        except Environment.DoesNotExist:
            context['status'], context['message'] = 'ERROR', 'Not found this Execution.'
            return context

        if exe.testexecution_set.count():
            context['status'], context['message'] = 'ERROR', 'This Execution has been used.'
        else:
            if exe.patch:
                file_name = MEDIA_PATH + "/" + str(exe.patch)
                count = Environment.objects.filter(project_id=project, patch=exe.patch).count()
                if count == 1:
                    # delete if only current exe uses the patch
                    if os.path.exists(file_name):
                        os.remove(file_name)
            exe.delete()
            context['status'], context['message'] = 'SUCCESS', ''

        return context

    @staticmethod
    def _search_exe(para, project, context):
        itec = para.get('itec', None)
        env_type = para.get('env_type', None)
        exe_name = para.get('exe_name', None)
        is_invalid = para.get('is_invalid', None)
        filter_param = {'project_id': project}

        if itec:
            filter_param['itec__name'] = itec
        if env_type:
            filter_param['env_type__name'] = env_type
        if exe_name:
            filter_param['name__icontains'] = exe_name
        if is_invalid:
            filter_param['is_invalid'] = is_invalid == str(True)

        context['exe_all'] = Environment.objects.filter(**filter_param).order_by('-id')
        context['status'] = 'SUCCESS'
        context['message'] = ''

        return context

    @staticmethod
    def _set_exe_status(para, project, context):
        exe = Environment.objects.get(id=para['id'])
        exe.is_invalid = para['is_invalid'] == str(True)
        exe.save()

        if exe.is_invalid is False:
            config = Configuration.objects.get(env_id=exe.id)
            payload = {
                'name': exe.name,
                'testplan': exe.testplan.name,
                'itec': exe.itec.ip,
                'worker': exe.worker,
                'owner': exe.owner,
                'os': config.os,
                'kernel': config.kernel,
                'gcc': config.gcc,
                'target': config.target,
                'nic': config.nic,
                'test_type': config.test_type,
                'driver': config.driver,
                'platform': config.platform,
                'env_type': exe.env_type.name,
                'schedule': exe.schedule,
                'start_time': exe.runtime,
                'git_repo': exe.git_repo,
                'commit_id': exe.commit_id,
                'patch': exe.patch,
                'package': exe.package,
                'user_email': para['user_email']
            }
            post_env_setting(payload)

        status, message = 'SUCCESS', ''
        context['message'] = message
        context['status'] = status
        return context

    @staticmethod
    def _get_itec_info(para, project, context):
        itec_id = para.get('itec_id', None)
        exe_id = para.get('exe_id', None)
        itec_ip = None
        worker = None

        if itec_id:
            # new env
            itec_obj = iTEC.objects.get(
                project_id=project,
                id=itec_id
            )
            itec_ip = itec_obj.ip
        if exe_id:
            # modify env
            exe_obj = Environment.objects.get(id=exe_id)
            itec_ip = exe_obj.itec.ip
            worker = exe_obj.worker

        worker_info = json.loads(get_itec_info(str(itec_ip)))
        process_data(context, worker_info, worker)

        status, message = 'SUCCESS', ''
        context['message'] = message
        context['status'] = status
        return context

    @staticmethod
    def _get_worker_info(para, project, context):
        worker = para.get('worker_name', None)
        worker_info = para.get('worker_info', None)
        process_data(context, worker_info, worker)

        status, message = 'SUCCESS', ''
        context['status'] = status
        context['message'] = message
        return context

    def _upload_patch(self, request, path, context):
        patch_name, status, message = '', '', ''
        exe_id = request.POST.get('exe_id', None)
        if request.method == 'POST':
            form = FileForm(request.FILES)
            f = form.data.get('patch')
            env = Environment.objects.get(id=exe_id)
            files = MEDIA_PATH + "/files/" + f.name
            if os.path.exists(files):
                f.name = env.name + "_" + f.name
            after_file = MEDIA_PATH + "/files/" + f.name
            if os.path.exists(after_file):
                os.remove(after_file)
            env.patch = f
            env.save()
        context['upload_status'], context['upload_message'] = status, message
        context['progress'] = 'done'
        context['patch_name'] = patch_name
        return context

    def _operate(self, method, param, project, context):
        # if method and para:
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = ExeInfo.objects.get(cmsplugin_ptr_id=instance)
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        context['path'] = config.path
        context['title'] = config.title
        context['size'] = config.size
        context['exe_all'] = Environment.objects.filter(project_id=project.id).order_by('-id')
        context['itec_list'] = iTEC.objects.filter(project_id=project.id)
        context['type_list'] = EnvironmentType.objects.filter(project_id=project.id)

        method = argpost.get('execution_method', None)
        parameters = argpost.get('execution_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)
        elif argpost:
            # upload patch
            self._upload_patch(context['request'], config.path, context)

        # paging processing
        exe_list, page_range, entry_num = paginator(argpost, context['exe_all'])
        exe_config_list = [{'exe': exe, 'config': exe.configuration_set.all()[0]} for exe in exe_list]

        context['exe_count'] = len(context['exe_all'])
        context['exe_config_list'] = exe_config_list
        context['exe_list'] = exe_list
        context['page_range'] = page_range
        context['entry_num'] = entry_num
        context['proj_name'] = project_name
        return context


class iTECPlugin(CMSPluginBase):
    name = 'itec_plugin'
    model = iTECInfo
    render_template = 'itec_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_itec(para, project, context):
        # check whether iTEC exist
        count = iTEC.objects.filter(
            name=para['itec_name'],
            project_id=project).count()

        if count:
            status, message = 'ERROR', 'This iTEC already exists.'
        else:
            iTEC.objects.create(
                name=para['itec_name'],
                ip=para['itec_ip'],
                project_id=project
            )
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_itec(para, project, context):
        # check whether iTEC exist
        count = iTEC.objects.filter(
            name=para['itec_name'],
            project_id=project).count()

        if count == 1:
            itec = iTEC.objects.get(
                name=para['itec_name'],
                project_id=project)

            if itec.id == int(para['id']):
                # modify without name
                itec.ip = para.get('itec_ip', None)
                itec.save()
                status, message = 'SUCCESS', ''
            else:
                status, message = 'ERROR', 'This iTEC already exists.'
        elif count == 0:
            itec = iTEC.objects.get(id=para['id'])
            itec.name = para['itec_name']
            itec.ip = para['itec_ip']
            itec.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_itec(para, project, context):
        try:
            itec = iTEC.objects.get(id=para['id'])
        except iTEC.DoesNotExist:
            context['status'], context['message'] = 'ERROR', 'Not found this app.'
            return context

        if itec.environment_set.count():
            context['status'], context['message'] = 'ERROR', 'This iTEC has been used.'
        else:
            itec.delete()
            context['status'], context['message'] = 'SUCCESS', ''
        return context

    @staticmethod
    def _search_itec(para, project, context):
        filter_param = {'project_id': project}
        itec_name = para.get('itec_name', None)
        if itec_name:
            filter_param['name__icontains'] = itec_name
        context['itec_all'] = iTEC.objects.filter(**filter_param).order_by('-id')

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_worker_detail(para, project, context):
        itec_id = para.get('itec_id', None)
        itec_obj = iTEC.objects.get(id=itec_id)
        worker_info = json.loads(get_itec_info(str(itec_obj.ip)))
        process_worker_detail(context, worker_info)

        context['store'] = 'store'
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    def _operate(self, method, param, project, context):
        # if method and para:
        para = json.loads(param)
        return eval('self.'+method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = iTECInfo.objects.get(cmsplugin_ptr_id=instance)
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        context['title'] = config.title
        context['size'] = config.size
        context['itec_all'] = iTEC.objects.filter(project_id=project.id).order_by('-id')

        method = argpost.get('itec_method', None)
        parameters = argpost.get('itec_para', None)

        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # Paging processing
        itec_list, page_range, entry_num = paginator(argpost, context['itec_all'])

        context['itec_count'] = len(context['itec_all'])
        context['itec_list'] = itec_list
        context['page_range'] = page_range
        context['entry_num'] = entry_num
        return context

plugin_pool.register_plugin(ExePlugin)
plugin_pool.register_plugin(iTECPlugin)
