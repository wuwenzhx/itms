from __future__ import division
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.http import QueryDict
from plugins.casecenter.models import *
from base_models.models import *
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from utils.decorators import check_login_required_flag
import operator
import json


def paginator(argpost, data):
    if data is None:
        return [], []
    after_range_num = 5
    before_range_num = 4

    # page = int(page)
    page = int(argpost.get('page', 1))
    entry_num = int(argpost.get('entry_num', 5))
    my_paginator = Paginator(data, entry_num)

    try:
        page_list = my_paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        page_list = my_paginator.page(my_paginator.num_pages)

    if page >= after_range_num:
        page_range = my_paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = my_paginator.page_range[0:page + before_range_num]

    return page_list, page_range, entry_num


class RequirementTypePlugin(CMSPluginBase):
    name = 'req_type_plugin'
    render_template = 'req_type_plugin.html'

    @staticmethod
    def _add_req_type(para, project):
        count = Type.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This type already exists.'
        else:
            req_type = Type.objects.create(
                name=para['name'],
                project_id=project
            )
            req_type.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _modify_req_type(para, project):
        count = Type.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This type already exists.'
        else:
            req_type = Type.objects.get(
                id=para['id'],
                project_id=project
            )
            req_type.name = para['name']
            req_type.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _delete_req_type(para, project):
        try:
            req_type = Type.objects.get(id=para['id'])
        except Type.DoesNotExist:
            status, message = 'ERROR', 'Not found this Type.'
            return status, message
        req_type.requirement_set.clear()
        Type.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()
        status, message = 'SUCCESS', ''
        return status, message

    def _operate(self, method, param, project):
        para = json.loads(param)
        if method and para:
            return eval('self.' + method)(para, project.id)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        status, message = None, None
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        method = argpost.get('req_type_method', None)
        parameters = argpost.get('req_type_para', None)
        if method and parameters:
            status, message = self._operate(method, parameters, project)

        type_list = Type.objects.filter(project_id=project.id)
        context['type_list'] = type_list
        context['status'] = status
        context['message'] = message
        return context


class RequirementPlugin(CMSPluginBase):
    model = RequirementInfo
    name = 'req_plugin'
    render_template = 'req_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_req(para, project, context):
        count = Requirement.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Requirement already exists.'
        else:
            req = Requirement.objects.create(
                name=para['name'],
                create_time=para['create_time'],
                owner=para['owner'],
                type_id=para.get('type_id', None),
                description=para['description'],
                project_id=project
            )
            req.save()
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_req(para, project, context):
        count = Requirement.objects.filter(name=para['name'], project_id=project).count()
        if count == 1:
            req = Requirement.objects.get(name=para['name'], project_id=project)
            if req.id == int(para['id']):
                # modify without name
                req.create_time = para['create_time']
                req.type_id = para.get('type_id', None)
                req.description = para['description']
                req.project_id = project
                req.save()
                status, message = 'SUCCESS', ''
            else:
               status, message = 'ERROR', 'This Requirement already exists.'
        elif count == 0:
            req = Requirement.objects.get(id=para['id'])
            req.name = para['name']
            req.create_time = para['create_time']
            req.type_id = para.get('type_id', None)
            req.description = para['description']
            req.project_id = project
            req.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_req(para, project, context):
        try:
            req = Requirement.objects.get(id=para['id'])
        except Requirement.DoesNotExist:
            context['status'] = 'ERROR'
            context['message'] = 'Not found this Requirement.'
            return context

        req.feature_set.clear()
        Requirement.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _search_req(para, project, context):
        req_type_name = para.get('req_type_name', None)
        req_name = para.get('req_name', None)

        filter_obj = {'project_id': project}
        if req_type_name:
            filter_obj['type__name'] = req_type_name
        if req_name:
            filter_obj['name__icontains'] = req_name

        context['req_all'] = Requirement.objects.filter(**filter_obj).order_by('-id')

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_data(para, project, context):
        # get related feature
        context['related_fea_list'] = Feature.objects.filter(requirement_id=para['req_id'])

        # get feature list
        fea_component_name = para.get('fea_component_name', None)
        fea_name = para.get('fea_name', None)
        req_type_name = para.get('req_type_name', None)
        req_name = para.get('req_name', None)

        filter_arg = {'project_id': project}
        if fea_name:
            filter_arg['name__icontains'] = fea_name
        if fea_component_name:
            filter_arg['component__name'] = fea_component_name
        if req_type_name:
            filter_arg['requirement__type__name'] = req_type_name
        if req_name:
            filter_arg['requirement__name'] = req_name

        fea_set = set(Feature.objects.filter(**filter_arg)) - set(context['related_fea_list'])
        context['fea_list'] = sorted(
            list(fea_set), key=operator.attrgetter('id'), reverse=True)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _modify_related_data(para, project, context):
        req = Requirement.objects.get(id=para['req_id'])
        req.feature_set.clear()
        for fea_id in para['related_data_id_list']:
            fea = Feature.objects.get(id=fea_id)
            req.feature_set.add(fea)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _cascade_filter(para, project, context):
        req_type_name = para.get('req_type_name', None)

        req_arg = {'project_id': project}
        if req_type_name:
            req_arg['type__name'] = req_type_name
        context['req_all_origin'] = Requirement.objects.filter(**req_arg)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_filter_data(para, project, context):
        context['req_all_origin'] = Requirement.objects.filter(project_id=project)
        context['fea_component_list'] = Component.objects.filter(project_id=project)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    def _operate(self, method, param, project, context):
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        config = RequirementInfo.objects.get(cmsplugin_ptr_id=instance)

        context['title'] = config.title
        context['size'] = config.size
        context['req_all'] = Requirement.objects.filter(
            project_id=project.id).order_by('-id')
        context['type_list'] = Type.objects.filter(project_id=project.id)

        method = argpost.get('req_method', None)
        parameters = argpost.get('req_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # Paging processing
        req_list, page_range, entry_num = paginator(argpost, context['req_all'])
        context['req_count'] = len(context['req_all'])
        context['req_list'] = req_list
        context['page_range'] = page_range
        context['entry_num'] = entry_num

        return context


class FeatureComponentPlugin(CMSPluginBase):
    name = 'fea_component_plugin'
    render_template = 'fea_component_plugin.html'

    @staticmethod
    def _add_feature_component(para, project):
        count = Component.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Component already exists.'
        else:
            fea_component = Component.objects.create(
                name=para['name'],
                project_id=project
            )
            fea_component.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _modify_feature_component(para, project):
        count = Component.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Component already exists.'
        else:
            fea_component = Component.objects.get(
                id=para['id'],
                project_id=project
            )
            fea_component.name = para['name']
            fea_component.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _delete_feature_component(para, project):
        try:
            fea_component = Component.objects.get(id=para['id'])
        except Component.DoesNotExist:
            status, message = 'ERROR', 'Not found this Component.'
            return status, message
        fea_component.feature_set.clear()
        Component.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()
        status, message = 'SUCCESS', ''
        return status, message

    def _operate(self, method, param, project):
        para = json.loads(param)
        if method and para:
            return eval('self.' + method)(para, project.id)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context
        status, message = None, None
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        method = argpost.get('fea_component_method', None)
        parameters = argpost.get('fea_component_para', None)
        if method and parameters:
            status, message = self._operate(method, parameters, project)

        component_list = Component.objects.filter(project_id=project.id)
        context['component_list'] = component_list
        context['status'] = status
        context['message'] = message
        return context


class FeaturePlugin(CMSPluginBase):
    model = FeatureInfo
    name = 'feature_plugin'
    render_template = 'feature_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_feature(para, project, context):
        count = Feature.objects.filter(name=para['name'],  project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Feature already exists.'
        else:
            fea = Feature.objects.create(
                name=para['name'],
                create_time=para['create_time'],
                owner=para.get('owner', None),
                description=para['description'],
                component_id=para.get('component_id', None),
                requirement_id=para.get('req_id', None),
                project_id=project
            )
            fea.save()
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_feature(para, project, context):
        count = Feature.objects.filter(name=para['name'],  project_id=project).count()
        if count == 1:
            fea = Feature.objects.get(name=para['name'],  project_id=project)
            if fea.id == int(para['id']):
                # modify without name
                fea.create_time = para['create_time']
                fea.description = para['description']
                fea.component_id = para.get('component_id', None)
                fea.requirement_id = para.get('req_id', None)
                fea.project_id = project
                fea.save()
                status, message = 'SUCCESS', ''
            else:
                status, message = 'ERROR', 'This Feature already exists.'
        elif count == 0:
            fea = Feature.objects.get(id=para['id'])
            fea.name = para['name']
            fea.create_time = para['create_time']
            fea.description = para['description']
            fea.component_id = para.get('component_id', None)
            fea.requirement_id = para.get('requirement_id', None)
            fea.project_id = project
            fea.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_feature(para, project, context):
        try:
            fea = Feature.objects.get(id=para['id'])
        except Feature.DoesNotExist:
            context['status'] = 'ERROR'
            context['message'] = 'Not found this feature.'
            return context
        fea.testcase_set.clear()
        Feature.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_data(para, project, context):
        # get related testcase list
        context['related_case_list'] = TestCase.objects.filter(
            feature_id=para['fea_id'], del_flag=False)

        # get testcase list
        req_type_name = para.get('req_type_name', None)
        req_name = para.get('req_name', None)
        fea_component_name = para.get('fea_component_name', None)
        fea_name = para.get('fea_name', None)
        performance = para.get('performance', None)
        case_type_name = para.get('case_type_name', None)
        case_name = para.get('case_name', None)

        filter_obj = {'del_flag': False, 'project_id': project}
        if req_type_name:
            filter_obj['feature__requirement__type__name'] = req_type_name
        if req_name:
            filter_obj['feature__requirement__name'] = req_name
        if fea_component_name:
            filter_obj['feature__component__name'] = fea_component_name
        if fea_name:
            filter_obj['feature__name'] = fea_name
        if case_type_name:
            filter_obj['type__name'] = case_type_name
        if performance:
            filter_obj['performance'] = performance == str(True)
        if case_name:
            filter_obj['name__icontains'] = case_name

        case_list = TestCase.objects.filter(**filter_obj)
        unrelated_case_set = set(case_list) - set(context['related_case_list'])
        context['case_list'] = sorted(
            list(unrelated_case_set), key=operator.attrgetter('id'), reverse=True)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _modify_related_data(para, project, context):
        fea = Feature.objects.get(id=para['fea_id'])
        fea.testcase_set.clear()
        for case_id in para['related_data_id_list']:
            case = TestCase.objects.get(id=case_id)
            fea.testcase_set.add(case)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _cascade_filter(para, project, context):
        cascade_obj = para.get('cascade_obj', None)
        req_type_name = para.get('req_type_name', None)
        fea_component_name = para.get('fea_component_name', None)

        req_arg = {'project_id': project}
        if cascade_obj == 'req_type':
            if req_type_name:
                req_arg['type__name'] = req_type_name
            context['req_list'] = Requirement.objects.filter(**req_arg)

        if cascade_obj == 'fea_component':
            if fea_component_name:
                req_arg['component__name'] = fea_component_name
            context['fea_all_origin'] = Feature.objects.filter(**req_arg)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _search_feature(para, project, context):
        req_type_name = para.get('req_type_name', None)
        req_name = para.get('req_name', None)
        fea_component_name = para.get('fea_component_name', None)
        fea_name = para.get('fea_name', None)

        filter_obj = {'project_id': project}
        if req_type_name:
            filter_obj['requirement__type__name'] = req_type_name
        if req_name:
            filter_obj['requirement__name'] = req_name
        if fea_component_name:
            filter_obj['component__name'] = fea_component_name
        if fea_name:
            filter_obj['name__icontains'] = fea_name

        context['fea_all'] = Feature.objects.filter(**filter_obj).order_by('-id')
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_filter_data(para, project, context):
        context['fea_all_origin'] = Feature.objects.filter(project_id=project)
        context['case_type_list'] = TestCaseType.objects.filter(project_id=project)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    def _operate(self, method, param, project, context):
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        config = FeatureInfo.objects.get(cmsplugin_ptr_id=instance)

        context['title'] = config.title
        context['size'] = config.size
        context['fea_component_list'] = Component.objects.filter(project_id=project.id)
        context['fea_all'] = Feature.objects.filter(project_id=project.id).order_by('-id')
        context['req_list'] = Requirement.objects.filter(project_id=project.id)
        context['req_type_list'] = Type.objects.filter(project_id=project.id)

        method = argpost.get('fea_method', None)
        parameters = argpost.get('fea_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # Paging processing
        fea_list, page_range, entry_num = paginator(argpost, context['fea_all'])
        context['fea_count'] = len(context['fea_all'])
        context['fea_list'] = fea_list
        context['page_range'] = page_range
        context['entry_num'] = entry_num

        return context


class TestcaseTypePlugin(CMSPluginBase):
    name = 'case_type_plugin'
    render_template = 'case_type_plugin.html'

    @staticmethod
    def _add_case_type(para, project):
        count = TestCaseType.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Type already exists.'
        else:
            case_type = TestCaseType.objects.create(
                name=para['name'],
                project_id=project
            )
            case_type.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _modify_case_type(para, project):
        count = TestCaseType.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Type already exists.'
        else:
            case_type = TestCaseType.objects.get(
                id=para['id'],
                project_id=project
            )
            case_type.name = para['name']
            case_type.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _delete_case_type(para, project):
        try:
            case_type = TestCaseType.objects.get(id=para['id'])
        except TestCaseType.DoesNotExist:
            status, message = 'ERROR', 'Not found this type.'
            return status, message
        case_type.testcase_set.clear()
        TestCaseType.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()
        status, message = 'SUCCESS', ''
        return status, message

    def _operate(self, method, param, project):
        para = json.loads(param)
        if method and para:
            return eval('self.' + method)(para, project.id)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context
        status, message = None, None
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        if argpost:
            method = argpost.get('case_type_method', None)
            parameters = argpost.get('case_type_para', None)
            if method and parameters:
                status, message = self._operate(method, parameters, project)
        type_list = TestCaseType.objects.filter(project_id=project.id)
        context['type_list'] = type_list
        context['status'] = status
        context['message'] = message
        return context


class TestCasePlugin(CMSPluginBase):
    model = TestCaseInfo
    name = 'testcase_plugin'
    render_template = 'testcase_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_testcase(para, project, context):
        count = TestCase.objects.filter(
            name=para['name'],
            del_flag=False,
            project_id=project).count()

        if count:
            status, message = 'ERROR', 'This test case already exists.'
        else:
            TestCase.objects.create(
                name=para['name'],
                type_id=para.get('type_id', None),
                description=para['description'],
                script_path=para['script_path'],
                config_path=para['config_path'],
                parameters=para['parameters'],
                feature_id=para.get('feature_id', None),
                performance=para['performance'] == str(True),
                app_id=para.get('app_id', None),
                project_id=project
            )
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_testcase(para, project, context):
        # check whether testcase exist
        count = TestCase.objects.filter(
            name=para['name'],
            del_flag=False,
            project_id=project).count()

        if count == 1:
            testcase = TestCase.objects.get(
                name=para['name'],
                project_id=project)

            if testcase.id == int(para['id']):
                # modify without name
                testcase.type_id = para.get('type_id', None)
                testcase.description = para['description']
                testcase.script_path = para['script_path']
                testcase.config_path = para['config_path']
                testcase.parameters = para['parameters']
                testcase.feature_id = para.get('feature_id', None)
                testcase.project_id = project
                testcase.save()
                status, message = 'SUCCESS', ''
            else:
                status, message = 'ERROR', 'This test case already exists.'
        elif count == 0:
            testcase = TestCase.objects.get(id=para['id'])
            testcase.name = para['name']
            testcase.type_id = para.get('type_id', None)
            testcase.description = para['description']
            testcase.script_path = para['script_path']
            testcase.config_path = para['config_path']
            testcase.parameters = para['parameters']
            testcase.feature_id = para.get('feature_id', None)
            testcase.project_id = project
            testcase.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_testcase(para, project, context):
        try:
            testcase = TestCase.objects.get(id=para['id'])
            testcase.del_flag = True
            testcase.testsuite.clear()
            testcase.save()
            status, message = 'SUCCESS', ''
        except TestCase.DoesNotExist:
            status, message = 'ERROR', 'Not found this test case.'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_related_data(para, project, context):
        testcase = TestCase.objects.get(id=para['case_id'])
        testcase.testsuite.clear()
        for suite_id in para['related_data_id_list']:
            suite = TestSuite.objects.get(id=suite_id)
            suite.testcase_set.add(testcase)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_data(para, project, context):
        # get related testsuite
        testcase = TestCase.objects.get(id=para['case_id'])
        subsystem_name = para.get('subsystem_name', None)
        suite_name = para.get('suite_name', None)

        filter_arg = {'project_id': project}
        if subsystem_name:
            filter_arg['subsystem__name'] = subsystem_name
        if suite_name:
            filter_arg['name__icontains'] = suite_name

        filter_arg['performance'] = testcase.performance
        filter_arg['app'] = testcase.app
        filter_arg['del_flag'] = False

        context['related_suite_list'] = testcase.testsuite.filter(del_flag=False)
        suite_list = TestSuite.objects.filter(**filter_arg)
        unrelated_suite_set = set(suite_list) - set(context['related_suite_list'])
        context['testsuite_list'] = sorted(
            list(unrelated_suite_set), key=operator.attrgetter('id'), reverse=True)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _cascade_filter(para, project, context):
        req_type_name = para.get('req_type_name', None)
        fea_component_name = para.get('fea_component_name', None)

        req_arg = {'project_id': project}
        if req_type_name and req_type_name != '':
            req_arg['type__name'] = req_type_name
        context['req_list'] = Requirement.objects.filter(**req_arg)

        fea_arg = {'project_id': project}
        if fea_component_name and fea_component_name != '':
            fea_arg['component__name'] = fea_component_name
        context['fea_list'] = Feature.objects.filter(**fea_arg)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _search_testcase(para, project, context):
        req_type_name = para.get('req_type_name', None)
        req_name = para.get('req_name', None)
        fea_component_name = para.get('fea_component_name', None)
        fea_name = para.get('fea_name', None)
        case_type_name = para.get('case_type_name', None)
        performance = para.get('performance', None)
        case_name = para.get('case_name', None)

        filter_obj = {'del_flag': False, 'project_id': project}
        if req_type_name:
            filter_obj['feature__requirement__type__name'] = req_type_name
        if req_name:
            filter_obj['feature__requirement__name'] = req_name
        if fea_component_name:
            filter_obj['feature__component__name'] = fea_component_name
        if fea_name:
            filter_obj['feature__name'] = fea_name
        if case_type_name:
            filter_obj['type__name'] = case_type_name
        if performance:
            filter_obj['performance'] = performance == str(True)
        if case_name:
            filter_obj['name__icontains'] = case_name

        context['testcase_all'] = TestCase.objects.filter(**filter_obj).order_by('-id')
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_filter_data(para, project, context):
        context['subsystem_list'] = Subsystem.objects.filter(project_id=project)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    def _operate(self, method, param, project, context):
        # if method and para:
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = TestCaseInfo.objects.get(cmsplugin_ptr_id=instance)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        argpost = QueryDict.dict(context['request'].POST)

        context['title'] = config.title
        context['size'] = config.size
        context['testcase_all'] = TestCase.objects.filter(
            del_flag=False, project_id=project.id).order_by('-id')
        context['req_type_list'] = Type.objects.filter(project_id=project.id)
        context['req_list'] = Requirement.objects.filter(project_id=project.id)
        context['fea_component_list'] = Component.objects.filter(project_id=project.id)
        context['fea_list'] = Feature.objects.filter(project_id=project.id)
        context['type_list'] = TestCaseType.objects.filter(project_id=project.id)
        context['app_list'] = App.objects.filter(project_id=project.id)

        method = argpost.get('testcase_method', None)
        parameters = argpost.get('testcase_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # Paging processing
        testcase_list, page_range, entry_num = paginator(argpost, context['testcase_all'])
        context['testcase_count'] = len(context['testcase_all'])
        context['testcase_list'] = testcase_list
        context['page_range'] = page_range
        context['entry_num'] = entry_num
        return context


class TestsuiteSubsystemPlugin(CMSPluginBase):
    name = 'suite_subsystem_plugin'
    render_template = 'suite_subsystem_plugin.html'

    @staticmethod
    def _add_suite_subsystem(para, project):
        count = Subsystem.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This subsystem already exists.'
        else:
            suite_subsystem = Subsystem.objects.create(
                name=para['name'],
                project_id=project
            )
            suite_subsystem.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _modify_suite_subsystem(para, project):
        count = Subsystem.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This subsystem already exists.'
        else:
            suite_subsystem = Subsystem.objects.get(
                id=para['id'],
                project_id=project
            )
            suite_subsystem.name = para['name']
            suite_subsystem.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _delete_suite_subsystem(para, project):
        try:
            suite_subsystem = Subsystem.objects.get(id=para['id'])
        except Subsystem.DoesNotExist:
            status, message = 'ERROR', 'Not found is subsystem.'
            return status, message
        suite_subsystem.testsuite_set.clear()
        Subsystem.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()
        status, message = 'SUCCESS', ''
        return status, message

    def _operate(self, method, param, project):
        para = json.loads(param)
        if method and para:
            return eval('self.' + method)(para, project.id)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context
        status, message = None, None
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        method = argpost.get('suite_subsystem_method', None)
        parameters = argpost.get('suite_subsystem_para', None)
        if method and parameters:
            status, message = self._operate(method, parameters, project)

        subsystem_list = Subsystem.objects.filter(project_id=project.id)
        context['subsystem_list'] = subsystem_list
        context['status'] = status
        context['message'] = message
        return context


class TestSuitePlugin(CMSPluginBase):
    model = TestSuiteInfo
    name = 'testsuite_plugin'
    render_template = 'testsuite_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_suite(para, project, context):
        count = TestSuite.objects.filter(
            name=para['name'],
            del_flag=False,
            project_id=project).count()

        if count:
            status, message = 'ERROR', 'This suite already exists.'
        else:
            TestSuite.objects.create(
                name=para['name'],
                subsystem_id=para.get('subsystem_id', None),
                description=para['description'],
                performance=para['performance'] == str(True),
                app_id=para.get('app_id', None),
                project_id=project
            )
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_suite(para, project, context):
        count = TestSuite.objects.filter(
            name=para['name'],
            del_flag=False,
            project_id=project).count()

        if count == 1:
            testsuite = TestSuite.objects.get(
                name=para['name'], project_id=project)
            if testsuite.id == int(para['id']):
                # modify without name
                testsuite.subsystem_id = para.get('subsystem_id', None)
                testsuite.description = para['description']
                testsuite.save()
                status, message = 'SUCCESS', ''
            else:
                status, message = 'ERROR', 'This suite already exists.'
        elif count == 0:
            testsuite = TestSuite.objects.get(id=para['id'])
            testsuite.name = para['name']
            testsuite.subsystem_id = para.get('subsystem_id', None)
            testsuite.description = para['description']
            testsuite.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_suite(para, project, context):
        try:
            testsuite = TestSuite.objects.get(id=para['id'])
            testsuite.del_flag = True
            testsuite.testplan.clear()
            testsuite.testcase_set.clear()
            testsuite.save()
            status, message = 'SUCCESS', ''
        except TestSuite.DoesNotExist:
            status, message = 'ERROR', 'Not found this test suite.'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_related_plan(para, project, context):
        testsuite = TestSuite.objects.get(id=para['suite_id'])
        testsuite.testplan.clear()
        for plan_id in para['related_plan_list']:
            testplan = TestPlan.objects.get(id=plan_id)
            testplan.testsuite_set.add(testsuite)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _modify_related_data(para, project, context):
        suite = TestSuite.objects.get(id=para['suite_id'])
        if para['related_obj'] == 'testcase':
            suite.testcase_set.clear()
            for case_id in para['related_data_id_list']:
                testcase = TestCase.objects.get(id=case_id)
                suite.testcase_set.add(testcase)

        if para['related_obj'] == 'testplan':
            suite.testplan.clear()
            for plan_id in para['related_data_id_list']:
                testplan = TestPlan.objects.get(id=plan_id)
                suite.testplan.add(testplan)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _search_suite(para, project, context):
        subsystem_name = para.get('subsystem_name', None)
        performance = para.get('performance', None)
        suite_name = para.get('suite_name', None)

        filter_obj = {'del_flag': False, 'project_id': project}
        if subsystem_name:
            filter_obj['subsystem__name'] = subsystem_name
        if performance:
            filter_obj['performance'] = performance == str(True)
        if suite_name:
            filter_obj['name__icontains'] = suite_name

        context['suite_all'] = TestSuite.objects.filter(**filter_obj).order_by('-id')
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _cascade_filter(para, project, context):
        cascade_obj = para.get('cascade_obj', None)
        req_type_name = para.get('req_type_name', None)
        fea_component_name = para.get('fea_component_name', None)

        req_arg = {'project_id': project}
        if cascade_obj == 'req_type':
            if req_type_name:
                req_arg['type__name'] = req_type_name
            context['req_list'] = Requirement.objects.filter(**req_arg)

        if cascade_obj == 'fea_component':
            if fea_component_name:
                req_arg['component__name'] = fea_component_name
            context['fea_list'] = Feature.objects.filter(**req_arg)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_data(para, project, context):
        suite = TestSuite.objects.get(id=para['suite_id'])
        filter_arg = {
            'performance': suite.performance,
            'app': suite.app,
            'del_flag': False,
            'project_id': project,
        }

        if para['related_obj'] == 'testcase':
            req_type_name = para.get('req_type_name', None)
            req_name = para.get('req_name', None)
            fea_component_name = para.get('fea_component_name', None)
            fea_name = para.get('fea_name', None)
            case_type_name = para.get('case_type_name', None)
            case_name = para.get('case_name', None)

            if req_type_name:
                filter_arg['feature__requirement__type__name'] = req_type_name
            if req_name:
                filter_arg['feature__requirement__name'] = req_name
            if fea_component_name:
                filter_arg['feature__component__name'] = fea_component_name
            if fea_name:
                filter_arg['feature__name'] = fea_name
            if case_type_name:
                filter_arg['type__name'] = case_type_name
            if case_name:
                filter_arg['name__icontains'] = case_name

            context['related_case_list'] = suite.testcase_set.filter(del_flag=False)
            case_list = TestCase.objects.filter(**filter_arg)
            unrelated_case_set = set(case_list) - set(context['related_case_list'])
            context['case_list'] = sorted(
                list(unrelated_case_set), key=operator.attrgetter('id'), reverse=True)

        if para['related_obj'] == 'testplan':
            plan_category_name = para.get('plan_category_name', None)
            plan_name = para.get('plan_name', None)

            if plan_category_name:
                filter_arg['category__name'] = plan_category_name
            if plan_name:
                filter_arg['name__icontains'] = plan_name

            context['related_plan_list'] = suite.testplan.filter(del_flag=False)
            plan_list = TestPlan.objects.filter(**filter_arg)
            unrelated_plan_set = set(plan_list) - set(context['related_plan_list'])
            context['plan_list'] = sorted(
                list(unrelated_plan_set), key=operator.attrgetter('id'), reverse=True)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_filter_data(para, project, context):
        context['req_type_list'] = Type.objects.filter(project_id=project)
        context['req_list'] = Requirement.objects.filter(project_id=project)
        context['fea_component_list'] = Component.objects.filter(project_id=project)
        context['fea_list'] = Feature.objects.filter(project_id=project)
        context['case_type_list'] = TestCaseType.objects.filter(project_id=project)
        context['category_list'] = Category.objects.filter(project_id=project)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    def _operate(self, method, param, project, context):
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        argpost = QueryDict.dict(context['request'].POST)
        config = TestSuiteInfo.objects.get(cmsplugin_ptr_id=instance)

        context['title'] = config.title
        context['size'] = config.size
        context['suite_all'] = TestSuite.objects.filter(
            del_flag=False, project_id=project.id).order_by('-id')
        context['subsystem_list'] = Subsystem.objects.filter(project_id=project.id)
        context['app_list'] = App.objects.filter(project_id=project.id)

        method = argpost.get('suite_method', None)
        parameters = argpost.get('suite_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # paging processing
        suite_list, page_range, entry_num = paginator(argpost, context['suite_all'])
        context['suite_count'] = len(context['suite_all'])
        context['suite_list'] = suite_list
        context["page_range"] = page_range
        context['entry_num'] = entry_num

        return context


class TestPlanPlugin(CMSPluginBase):
    model = TestPlanInfo
    name = 'testplan_plugin'
    render_template = 'testplan_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_plan(para, project, context):
        count = TestPlan.objects.filter(
            name=para['name'],
            del_flag=False,
            project_id=project).count()

        if count:
            status, message = 'ERROR', 'This plan already exists.'
        else:
            TestPlan.objects.create(
                name=para['name'],
                category_id=para.get('category_id', None),
                owner=para.get('owner', None),
                create_time=para['create_time'],
                start_time=para['start_time'],
                end_time=para['end_time'],
                performance=para['performance'] == str(True),
                app_id=para.get('app_id', None),
                description=para['description'],
                project_id=project
            )
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_plan(para, project, context):
        count = TestPlan.objects.filter(
            name=para['name'],
            del_flag=False,
            project_id=project).count()

        if count == 1:
            testplan = TestPlan.objects.get(
                name=para['name'],
                project_id=project
            )
            if testplan.id == int(para['id']):
                # modify without name
                testplan.category_id = para.get('category_id', None)
                testplan.create_time = para['create_time']
                testplan.start_time = para['start_time']
                testplan.end_time = para['end_time']
                testplan.description = para['description']
                testplan.save()
                status, message = 'SUCCESS', ''
            else:
                status, message = 'ERROR', 'This testplan already exists.'
        elif count == 0:
            testplan = TestPlan.objects.get(id=para['id'])
            testplan.name = para['name']
            testplan.category_id = para.get('category_id', None)
            testplan.create_time = para['create_time']
            testplan.start_time = para['start_time']
            testplan.end_time = para['end_time']
            testplan.description = para['description']
            testplan.save()
            status, message = 'SUCCESS', ''
        else:
            status, message = 'ERROR', '@#$%*&^%$#'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_plan(para, project, context):
        try:
            testplan = TestPlan.objects.get(id=para['id'])
            testplan.del_flag = True
            testplan.testsuite_set.clear()
            testplan.save()
            status, message = 'SUCCESS', ''
        except TestPlan.DoesNotExist:
            status, message = 'ERROR', 'Not found this test plan.'

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_related_data(para, project, context):
        plan = TestPlan.objects.get(id=para['plan_id'])
        plan.testsuite_set.clear()

        for suite_id in para['related_data_id_list']:
            suite = TestSuite.objects.get(id=suite_id)
            suite.testplan.add(plan)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_data(para, project, context):
        # get related testsuite
        plan = TestPlan.objects.get(id=para['plan_id'])
        context['related_suite_list'] = plan.testsuite_set.filter(del_flag=False)
        subsystem_name = para.get('subsystem_name', None)
        suite_name = para.get('suite_name', None)

        filter_arg = {
            'performance': plan.performance,
            'app': plan.app,
            'del_flag': False,
            'project_id': project,
        }
        if subsystem_name:
            filter_arg['subsystem__name'] = subsystem_name
        if suite_name:
            filter_arg['name__icontains'] = suite_name

        suite_list = TestSuite.objects.filter(**filter_arg)
        unrelated_suite_set = set(suite_list) - set(context['related_suite_list'])
        context['suite_list'] = sorted(
            list(unrelated_suite_set), key=operator.attrgetter('id'), reverse=True)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _search_plan(para, project, context):
        category_name = para.get('category_name', None)
        performance = para.get('performance', None)
        plan_name = para.get('plan_name', None)

        filter_obj = {'del_flag': False, 'project_id': project}
        if category_name:
            filter_obj['category__name'] = category_name
        if performance:
            filter_obj['performance'] = performance == str(True)
        if plan_name:
            filter_obj['name__icontains'] = plan_name

        context['plan_all'] = TestPlan.objects.filter(**filter_obj).order_by('-id')
        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _get_related_filter_data(para, project, context):
        context['subsystem_list'] = Subsystem.objects.filter(project_id=project)

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    def _operate(self, method, param, project, context):
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = TestPlanInfo.objects.get(cmsplugin_ptr_id=instance)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        argpost = QueryDict.dict(context['request'].POST)

        context['title'] = config.title
        context['size'] = config.size
        context['plan_all'] = TestPlan.objects.filter(
            del_flag=False, project_id=project.id).order_by('-id')
        context['category_list'] = Category.objects.filter(project_id=project.id)
        context['app_list'] = App.objects.filter(project_id=project.id)

        method = argpost.get('plan_method', None)
        parameters = argpost.get('plan_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # paging processing
        plan_list, page_range, entry_num = paginator(argpost, context['plan_all'])
        context['plan_count'] = len(context['plan_all'])
        context['plan_list'] = plan_list
        context["page_range"] = page_range
        context['entry_num'] = entry_num

        return context


class TestPlanCategoryPlugin(CMSPluginBase):
    name = 'testplan_category_plugin'
    render_template = 'testplan_category_plugin.html'

    @staticmethod
    def _add_plan_category(para, project):
        count = Category.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Category already exists.'
        else:
            plan_category = Category.objects.create(
                name=para['name'],
                project_id=project
            )
            plan_category.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _modify_plan_category(para, project):
        count = Category.objects.filter(name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This Category already exists.'
        else:
            plan_category = Category.objects.get(
                id=para['id'],
                project_id=project
            )
            plan_category.name = para['name']
            plan_category.save()
            status, message = 'SUCCESS', ''
        return status, message

    @staticmethod
    def _delete_plan_category(para, project):
        try:
            plan_category = Category.objects.get(id=para['id'])
        except:
            status, message = 'ERROR', 'Not found this Category.'
            return status, message
        plan_category.testplan_set.clear()
        Category.objects.filter(
            id=para['id'],
            project_id=project
        ).delete()
        status, message = 'SUCCESS', ''
        return status, message

    def _operate(self, method, param, project):
        para = json.loads(param)
        if method and para:
            return eval('self.' + method)(para, project.id)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context
        status, message = None, None
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)
        if argpost:
            method = argpost.get('plan_category_method', None)
            parameters = argpost.get('plan_category_para', None)
            if method and parameters:
                status, message = self._operate(method, parameters, project)
        category_list = Category.objects.filter(project_id=project.id)
        context['category_list'] = category_list
        context['status'] = status
        context['message'] = message
        return context


class AppPlugin(CMSPluginBase):
    name = 'app_plugin'
    model = AppInfo
    render_template = 'app_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _add_app(para, project, context):
        count = App.objects.filter(
            name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This app already exists.'
        else:
            App.objects.create(
                name=para['name'],
                project_id=project
            )
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_app(para, project, context):
        count = App.objects.filter(
            name=para['name'], project_id=project).count()
        if count:
            status, message = 'ERROR', 'This app already exists.'
        else:
            app = App.objects.get(id=para['id'])
            app.name = para['name']
            app.save()
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_app(para, project, context):
        try:
            app = App.objects.get(id=para['id'])
        except App.DoesNotExist:
            context['status'], context['message'] = 'ERROR', 'Not found this app.'
            return context

        if app.testcase_set.count() or app.testsuite_set.count() or \
                app.testplan_set.count() or app.testexecution_set.count():
            context['status'], context['message'] = 'ERROR', 'This app has been used.'
        else:
            app.delete()
            context['status'], context['message'] = 'SUCCESS', ''

        return context

    @staticmethod
    def _search_app(para, project, context):
        filter_param = {'project_id': project}
        app_name = para.get('app_name', None)
        if app_name:
            filter_param['name__icontains'] = app_name
        context['app_all'] = App.objects.filter(**filter_param).order_by('-id')

        context['status'] = 'SUCCESS'
        context['message'] = ''
        return context

    @staticmethod
    def _add_app_attr(para, project, context):
        count = AppAttr.objects.filter(
            name=para['name'],
            app_id=para['app_id'],
            project_id=project).count()
        if count:
            status, message = 'ERROR', 'This attribute already exists.'
        else:
            AppAttr.objects.create(
                name=para['name'],
                app_id=para['app_id'],
                project_id=project
            )
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _modify_app_attr(para, project, context):
        count = AppAttr.objects.filter(
            name=para['name'],
            app_id=para['app_id'],
            project_id=project).count()
        if count:
            status, message = 'ERROR', 'This attribute already exists.'
        else:
            attr = AppAttr.objects.get(id=para['id'])
            attr.name = para['name']
            attr.save()
            status, message = 'SUCCESS', ''

        context['status'] = status
        context['message'] = message
        return context

    @staticmethod
    def _delete_app_attr(para, project, context):
        try:
            attr = AppAttr.objects.get(id=para['id'])
        except AppAttr.DoesNotExist:
            context['status'], context['message'] = 'ERROR', 'Not found this attribute.'
            return context

        app = App.objects.get(id=attr.app_id)
        if app.testcase_set.count() or app.testsuite_set.count() or \
                app.testplan_set.count() or app.testexecution_set.count():
            context['status'], context['message'] = 'ERROR', 'This attribute has been used.'
        else:
            attr.delete()
            context['status'], context['message'] = 'SUCCESS', ''
        return context

    def _operate(self, method, param, project, context):
        para = json.loads(param)
        return eval('self.' + method)(para, project.id, context)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = AppInfo.objects.get(cmsplugin_ptr_id=instance)
        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        context['title'] = config.title
        context['size'] = config.size
        context['app_all'] = App.objects.filter(project_id=project.id).order_by('-id')

        method = argpost.get('app_method', None)
        parameters = argpost.get('app_para', None)
        if method and parameters:
            context = self._operate(method, parameters, project, context)

        # paging processing
        app_list, page_range, entry_num = paginator(argpost, context['app_all'])
        app_detail = [{'app': app, 'attr': app.appattr_set.all()} for app in app_list]

        context['app_detail'] = app_detail
        context['app_count'] = len(context['app_all'])
        context['entry_num'] = entry_num
        context['page_range'] = page_range
        context['app_list'] = app_list
        return context

plugin_pool.register_plugin(RequirementTypePlugin)
plugin_pool.register_plugin(RequirementPlugin)
plugin_pool.register_plugin(FeatureComponentPlugin)
plugin_pool.register_plugin(FeaturePlugin)
plugin_pool.register_plugin(TestcaseTypePlugin)
plugin_pool.register_plugin(TestCasePlugin)
plugin_pool.register_plugin(TestsuiteSubsystemPlugin)
plugin_pool.register_plugin(TestSuitePlugin)
plugin_pool.register_plugin(TestPlanPlugin)
plugin_pool.register_plugin(TestPlanCategoryPlugin)
plugin_pool.register_plugin(AppPlugin)
