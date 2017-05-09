from __future__ import division
from cms.plugin_base import CMSPluginBase
from django.core.exceptions import ObjectDoesNotExist
from cms.plugin_pool import plugin_pool
from django.http import QueryDict
from plugins.report.models import *
from base_models.models import *
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from utils.decorators import check_login_required_flag
import json
import operator
import ast
from collections import defaultdict
import time
def paginator(page, data):
    after_range_num = 5
    before_range_num = 4

    my_paginator = Paginator(data, 10)
    try:
        page_list = my_paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        page_list = my_paginator.page(my_paginator.num_pages)

    if page >= after_range_num:
        page_range = my_paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = my_paginator.page_range[0:page + before_range_num]

    return page_list, page_range


def get_config_size(size):
    extra = {}
    try:
        height, width = size.split('*')
    except:
        raise NameError

    if '%' not in height:
        height += "px"
    if '%' not in width:
        width += "px"
    extra['height'], extra['width'] = height, width

    return extra


def get_passrate(pass_number, total_number):
    if total_number <= 0:
        return 0
    return round((pass_number / total_number) * 100, 2)


class TestplanReportPlugin(CMSPluginBase):
    name = 'testplan_report_plugin'
    render_template = 'testplan_report_plugin.html'

    @staticmethod
    def _get_plan(argpost, project, is_perf):
        category_id = argpost.get('category_id', None)
        app_id = argpost.get('app_id', None)
        plan_name = argpost.get('testplan_name', None)

        plan_all = TestPlan.objects.all()
            #performance=is_perf,
            #del_flag=False,
            #project_id=project
        #)

        category_plan = app_plan = name_plan = plan_all
        if category_id:
            category_plan = TestPlan.objects.filter(
                #category_id=category_id,
                del_flag=False,
                project_id=project
            )
        if app_id:
            app_plan = TestPlan.objects.filter(
                #app_id=app_id,
                del_flag=False,
                project_id=project
            )
        if plan_name:
            name_plan = TestPlan.objects.filter(
                name__icontains=plan_name,
                del_flag=False,
                project_id=project
            )

        plan_list = list(set(category_plan) & set(app_plan) & set(name_plan))
        return sorted(plan_list, key=operator.attrgetter('id'), reverse=True)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        category_list = Category.objects.filter(project_id=project.id)
        nic_name_list = NicName.objects.filter(project_id=project.id)
        if 'performance' in context['request'].path:
            app_list = App.objects.filter(project_id=project.id)
            is_perf = True
        else:
            app_list = None
            is_perf = False

        plan_all = self._get_plan(argpost, project.id, is_perf)
        page = int(argpost.get('page', 1))
        plan_list, page_range = paginator(page, plan_all)

        context['plan_all'] = plan_all
        context['plan_list'] = plan_list
        context['category_list'] = category_list
        context['page_range'] = page_range
        context['app_list'] = app_list
        context['nic_name_list'] = nic_name_list

        return context

############ NIC TestplanReportPlugin ###########
class NicTestplanReportPlugin(CMSPluginBase):
    name = 'nic_testplan_report_plugin'
    render_template = 'nic_testplan_report_plugin.html'

    @staticmethod
    def _get_plan(argpost, project):
        nic_name_id = argpost.get('nic_name_id', None)
        cpu_type_id = argpost.get('cpu_type_id', None)
        firmware_id = argpost.get('firmware_id',None)
        case_type_id = argpost.get('case_type_id',None)
        device_id = argpost.get('device_id',None)
        plan_name = argpost.get('testplan_name', None)

        plan_all = TestRecordTable.objects.filter(
            project_id=project
        )

        device_id_plan= category_plan = firmware_plan = nic_name_plan =cpu_type_plan = name_plan = case_type_plan =plan_all
        if nic_name_id:
            nic_name_plan = TestRecordTable.objects.filter(
                nic_name_id=nic_name_id,
                project_id=project
            )
        if plan_name:
            name_plan = TestPlan.objects.filter(
                name__icontains=plan_name,
                del_flag=False,
                project_id=project
            )
        if firmware_id:
            firmware_plan = TestRecordTable.objects.filter(
                firmware_id=firmware_id,
                project_id=project
            )
        if cpu_type_id:
            cpu_type_plan = TestRecordTable.objects.filter(
                cpu_info_id=cpu_type_id,
                project_id=project
            )
        if case_type_id:
            case_type_plan = TestRecordTable.objects.filter(
                case_type_id=case_type_id,
                project_id=project
            )
        if device_id:
            device_id_plan = TestRecordTable.objects.filter(
                device_id=device_id,
                project_id=project
            )

        plan_list = list(set(nic_name_plan) & set(cpu_type_plan) & set(firmware_plan) & set(name_plan) & set(case_type_plan) &set(device_id_plan))
        
        return sorted(plan_list, key=operator.attrgetter('id'), reverse=True)
        
    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        cpu_type_list =CpuType.objects.filter(project_id=project.id)
        case_type_list= CaseType.objects.filter(project_id=project.id)
        nic_name_list = NicName.objects.filter(project_id=project.id)
        firmware_list = Firmware.objects.filter(project_id=project.id)
        device_id_list = DeviceId.objects.filter(project_id=project.id)

        page = int(argpost.get('page', 1))
        plan_all = self._get_plan(argpost, project.id)
        plan_list, page_range = paginator(page, plan_all)
        context['cpu_type_list'] = cpu_type_list
        context['nic_name_list'] = nic_name_list
        context['firmware_list'] = firmware_list
        context['case_type_list'] = case_type_list
        context['device_id_list'] = device_id_list
        context['page_range'] = page_range
        context['plan_list'] = plan_list
        return context


###### SPDK Testplan #######
class SpdkTestplanReportPlugin(CMSPluginBase):
    name = 'spdktestplan_report_plugin'
    render_template = 'spdk_testplan_plugin.html'

    @staticmethod
    def _get_plan(argpost, project, is_perf):
        queue_depth_id = argpost.get('queue_depth_id', None)
        rw_method_id = argpost.get('rw_method_id', None)
        create_time = argpost.get('create_time', None)
        end_time = argpost.get('end_time',None)
        plan_name = argpost.get('testplan_name', None)

        plan_all = TestPlan.objects.filter(
            #performance=is_perf,
            del_flag=False,
            project_id=project
        )

        queue_depth_plan = rw_method_plan = time_plan = name_plan = plan_all
        if queue_depth_id:
            queue_depth_plan = TestPlan.objects.filter(
                queue_depth_id=queue_depth_id,
                del_flag=False,
                project_id=project
            )
        if rw_method_id:
            rw_method_plan = TestPlan.objects.filter(
                rw=rw_method_id,
                del_flag=False,
                project_id=project
            )
        if create_time:
            time_plan = TestPlan.objects.filter(
                #pub_data__range=(create_time,end_time),
                #create_time.strftime("%y-%m-%d")=create_time,
                create_time__gte=create_time,
                #create_time__lt=create_time.date(strtotime(date("Y-m-d")."+1 day"))
                #pub_data__range=(create_time,create_time),
                project_id=project
            )
       # if end_time:
       #     time_plan1=TestPlan.objects.filter(
       #         create_time__lte=end_time,
       #         project_id=project
       #             )
        if plan_name:
            name_plan = TestPlan.objects.filter(
                name__icontains=plan_name,
                del_flag=False,
                project_id=project
            )

        plan_list = list(set(queue_depth_plan) & set(time_plan) & set(name_plan) &set(rw_method_plan))
        return sorted(plan_list, key=operator.attrgetter('id'), reverse=True)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        argpost = QueryDict.dict(context['request'].POST)
        project_name = context['request'].session['project']
        project = Project.objects.get(name=project_name)

        #category_list = Category.objects.filter(project_id=project.id)
        if 'performance' in context['request'].path:
            app_list = App.objects.filter(project_id=project.id)
            is_perf = True
        else:
            app_list = None
            is_perf = False
        create_time_list = Spdk_Perf_Result.objects.all()
        queue_depth_list= Queue_depth.objects.all()
        rw_method_list= Rw_method.objects.filter(project_id=project.id)
        plan_all = self._get_plan(argpost, project.id, is_perf)

        page = int(argpost.get('page',1))
        plan_list, page_range = paginator(page, plan_all)
        spdk = plan_all
        context['plan_all'] = plan_all
        context['plan_list'] = plan_list
        #context['category_list'] = category_list
        context['page_range'] = page_range
        context['app_list'] = app_list
        context['create_time_list']= create_time_list
        context['spdk'] = spdk
        context['queue_depth_list'] = queue_depth_list
        context['rw_method_list'] = rw_method_list
        return context


class RegularReportChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'regular_chart_plugin'
    render_template = 'regular_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        platform_list = Platform.objects.filter(
            project_id=project.id
        )

        os_list = OS.objects.filter(
            project_id=project.id
        )

        plan_id = argget.get("plan_id", None)
        os_id = argpost.get("os_id", None)
        platform_id = argpost.get("platform_id", None)
        chart_data = None

        if os_id and platform_id:
            exec_list = TestExecution.objects.filter(
                os_id=os_id,
                platform=platform_id,
                testplan_id=plan_id,
                project_id=project.id
            )
        elif os_id:
            exec_list = TestExecution.objects.filter(
                os_id=os_id,
                testplan_id=plan_id,
                project_id=project.id
            )
        elif platform_id:
            exec_list = TestExecution.objects.filter(
                platform=platform_id,
                testplan_id=plan_id,
                project_id=project.id
            )
        else:
            exec_list = TestExecution.objects.filter(
                testplan_id=plan_id,
                project_id=project.id
            )

        exe_array, pass_array, fail_array, rate_array = [], [], [], []
        for exe in exec_list:
            exe_array.append(exe.name)
            results = TestSuiteResult.objects.filter(
                testexecution_id=exe.id,
                project_id=project.id
            )

            pass_num, fail_num, total_num = 0, 0, 0
            for res in results:
                pass_num += res.passed
                fail_num += res.failed
                total_num += res.total

            pass_array.append(pass_num)
            fail_array.append(fail_num)
            rate_array.append(get_passrate(pass_num, total_num))

        if len(exec_list) > 0:
            chart_data = json.dumps({
                'exe_array': exe_array,
                'exec_length': len(exec_list),
                'rate_array': rate_array,
                'pass_array': pass_array,
                'fail_array': fail_array
            })

        context['chart_data'] = chart_data
        context['platform_list'] = platform_list
        context['os_list'] = os_list
        context['exec_list'] = exec_list
        return context


class RegularReportPlugin(CMSPluginBase):
    model = RegularReportInfo
    name = 'regular_report_plugin'
    render_template = 'regular_report_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _get_fail_result(exe_id_list):
        exe_result_dict = {}
        key_list, exe_name_list = [], []
        for exe_id in exe_id_list:
            exe_name_list.append(TestExecution.objects.get(id=exe_id).name)
            result_list = TestCaseResult.objects.filter(testsuite_result__testexecution__id=exe_id)
            result_dict = {}
            for r in result_list:
                result_dict[(r.testcase.id, r.testcase.name,
                             r.testsuite_result.testsuite.id, r.testsuite_result.testsuite.name
                             )] = r.result
                if (
                    r.testcase.id, r.testcase.name,
                    r.testsuite_result.testsuite.id, r.testsuite_result.testsuite.name
                ) not in key_list:
                    key_list.append((
                        r.testcase.id, r.testcase.name,
                        r.testsuite_result.testsuite.id, r.testsuite_result.testsuite.name))
            exe_result_dict[exe_id] = result_dict

        result_list = []
        for key in key_list:
            r_tmp_list = []
            for exe_id in exe_id_list:
                r_tmp_list.append(exe_result_dict[exe_id].get(key, ''))
            if 'fail' in r_tmp_list:
                tmp_list = list(key) + r_tmp_list
                result_list.append(tmp_list)
        return result_list, exe_name_list

    @staticmethod
    def _get_detail_result(argpost, project):
        suite_result_id = argpost.get('suite_result_id', None)
        view_result = argpost.get('view_result', None)

        if view_result:
            # get 'pass'/'fail'/'block'/'na'/no_run result's testcase
            detail_result = TestCaseResult.objects.filter(
                testsuite_result_id=suite_result_id,
                result=view_result.lower(),
                project_id=project.id)
        else:
            # get all run testcase
            detail_result = TestCaseResult.objects.filter(
                testsuite_result_id=suite_result_id,
                project_id=project.id)

        return detail_result

    @staticmethod
    def _get_chart_data(result_all):
        suite = {}
        suite_name, pie_list, circle_list = [], [], []

        for res in result_all:
            suite_name.append(res.testsuite.name)
            pie_list.append({
                'value': res.total,
                'name': res.testsuite.name
            })

            pass_rate = get_passrate(res.passed, res.total)
            fail_rate = get_passrate(res.failed, res.total)
            block_rate = get_passrate(res.block, res.total)
            na_rate = get_passrate(res.na, res.total)
            no_run_rate = get_passrate(res.no_run, res.total)

            circle_list.append({
                'name': res.testsuite.name,
                'passed': res.passed,
                'failed': res.failed,
                'block': res.block,
                'na': res.na,
                'no_run': res.no_run,
                'total': res.total,
                'pass_rate': pass_rate,
                'fail_rate': fail_rate,
                'block_rate': block_rate,
                'na_rate': na_rate,
                'no_run_rate': no_run_rate
            })

        suite['suite_name'] = suite_name
        suite['pie_list'] = pie_list
        suite['circle_list'] = circle_list
        return json.dumps(suite)

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportInfo.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        result_list = None
        result_all = None
        suite_page_range = None
        suite_chart_data = None

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)
        exec_all = TestExecution.objects.filter(
            testplan_id=plan_id,
            project_id=project.id
        ).order_by('-id')

        for exe in exec_all:
            results = TestSuiteResult.objects.filter(
                testexecution_id=exe.id,
                project_id=project.id
            )
            pass_num, total_num = 0, 0
            for res in results:
                pass_num += res.passed
                total_num += res.total
            exe.passrate = get_passrate(pass_num, total_num)
            exe.total = total_num

        execution_page = int(argpost.get('execution_page', 1))
        exec_list, exec_page_range = paginator(execution_page, exec_all)

        # view suite list
        execution_id = argpost.get("execution_id", None)
        if execution_id:
            result_all = TestSuiteResult.objects.filter(
                testexecution_id=execution_id,
                project_id=project.id
            )

            suite_page = int(argpost.get('suite_page', 1))
            result_list, suite_page_range = paginator(suite_page, result_all)
            suite_chart_data = self._get_chart_data(result_all)

        # compare execution result
        fail_result_list, exe_name_list = None, None
        selected_exe_id = argpost.get('selected_exe_id', None)
        if selected_exe_id:
            exe_id_list = json.loads(selected_exe_id)
            fail_result_list, exe_name_list = self._get_fail_result(exe_id_list)

        # view suite detail result
        detail_result_all = self._get_detail_result(
            argpost, project)
        suite_detail_page = int(argpost.get('suite_detail_page', 1))
        detail_result_list, suite_detail_page_range = paginator(
            suite_detail_page, detail_result_all)

        context['suite_result_chart_data'] = suite_chart_data
        context['suite_result_list'] = result_list
        context['suite_result_all'] = result_all
        context['exec_list'] = exec_list
        context['exec_all'] = exec_all
        context['exec_page_range'] = exec_page_range
        context['suite_page_range'] = suite_page_range
        context['fail_result_list'] = fail_result_list
        context['detail_result_list'] = detail_result_list
        context['detail_result_all'] = detail_result_all
        context['suite_detail_page_range'] = suite_detail_page_range
        context['exe_name_list'] = exe_name_list

        return context


class UndatedReportChartPlugin(CMSPluginBase):
    model = UndatedReportChart
    name = 'undated_chart_plugin'
    render_template = 'undated_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = UndatedReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        chart_data = None
        plan_id = argget.get("plan_id", None)
        try:
            execution = TestExecution.objects.get(
                testplan_id=plan_id,
                project_id=project.id
            )
        except TestExecution.DoesNotExist:
            execution = None

        if execution:
            suite_result = TestSuiteResult.objects.filter(
                testexecution_id=execution.id,
                project_id=project.id
            )
        else:
            suite_result = []

        suite_name_array, pass_array, fail_array = [], [], []
        for result in suite_result:
            suite_name_array.append(result.testsuite.name)
            pass_array.append(result.passed)
            fail_array.append(result.failed)

        if len(suite_name_array) > 0:
            chart_data = json.dumps({
                'suite_name_array': suite_name_array,
                'pass_array': pass_array,
                'fail_array': fail_array
            })

        context['chart_data'] = chart_data
        return context


class UndatedReportPlugin(CMSPluginBase):
    model = UndatedReportInfo
    name = 'undated_report_plugin'
    render_template = 'undated_report_plugin.html'
    fields = ('title', 'size')

    @staticmethod
    def _get_suite_result(plan_id, project):
        suite_result = []
        try:
            execution = TestExecution.objects.get(
                testplan_id=plan_id,
                project_id=project.id
            )
        except TestExecution.DoesNotExist:
            execution = None

        if execution:
            suite_result = TestSuiteResult.objects.filter(
                testexecution_id=execution.id,
                project_id=project.id
            )

        return suite_result

    @staticmethod
    def _get_detail_result(argpost, project):
        suite_result_id = argpost.get('suite_result_id', None)
        view_result = argpost.get('view_result', None)

        if view_result:
            # get 'pass'/'fail'/'block'/'na' result's testcase
            detail_result = TestCaseResult.objects.filter(
                testsuite_result_id=suite_result_id,
                result=view_result.lower(),
                project_id=project.id)
        else:
            # get all run testcase
            detail_result = TestCaseResult.objects.filter(
                testsuite_result_id=suite_result_id,
                project_id=project.id)

        return detail_result

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = UndatedReportInfo.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)

        # get suite result
        suite_result_all = self._get_suite_result(plan_id, project)
        suite_page = int(argpost.get('suite_page', 1))
        suite_result_list, suite_page_range = paginator(suite_page, suite_result_all)

        context['suite_result_all'] = suite_result_all
        context['suite_result_list'] = suite_result_list
        context['suite_page_range'] = suite_page_range

        # view suite detail result
        detail_result_all = self._get_detail_result(argpost, project)
        suite_detail_page = int(argpost.get('suite_detail_page', 1))
        detail_result_list, detail_page_range = paginator(suite_detail_page, detail_result_all)

        context['detail_result_all'] = detail_result_all
        context['detail_result_list'] = detail_result_list
        context['detail_page_range'] = detail_page_range
        print context
        return context


class PerfRegularReportPlugin(CMSPluginBase):
    model = PerfRegularReportInfo
    name = 'perf_regular_report_plugin'
    render_template = 'perf_regular_report_plugin.html'
    fields = ('title', 'size')

    '''
    def render(self, context, instance, placeholder):
        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)
        exe_id = argget.get("exe_id",None)
        chart_data = None
        exe_array,time_array,iops_array,latency_array,result_iops =[],[],[],[],[] 
        exec_list = TestExecution.objects.filter(testplan_id=plan_id,project_id=project.id)
        for exe in exec_list:
            exe_array.append(exe.name)
            results = Spdk_Perf_Result.objects.filter(
                testexecution_id=exe.id,
            )
            for res in results:
                iops_array.append(res.iops)
                latency_array.append(res.latency)
        time_list = Spdk_Perf_Result.objects.filter(project_id=project.id)
        #time_list = Spdk_Perf_Result.objects.all()
        for time in time_list:
            time_array.append(time.create_time)
        #iops_list=Spdk_Perf_Result.objects.filter(testexecution_id=exe_id)
        #iops_list=Spdk_Perf_Result.objects.all()
        #for iops in iops_list:
        #for iops in result_iops:
            #iops_array.append(iops.iops)
        #    iops_array.append(iops.iops)
            #latency_array.append(iops.latency)
        #    latency_array.append(iops.latency)
        if len(exec_list)>0:
            suite_result_chart_data = json.dumps({
                'exe_array':exe_array,
                'exec_length':len(exec_list),
                'iops_array': iops_array,
                'latency_array': latency_array,
                'time_array':'time_array',
            })
        
        context['suite_result_chart_data'] = suite_result_chart_data
        #context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        return context
        '''
    @staticmethod
    def _get_spdk_exe_result(context,argpost,plan_id,project):
        result_list = Spdk_Perf_Result.objects.all()
        iops_list=[]
        latency_list=[]
        for res in result_list:
            iops_list.append(res.iops)
            latency_liat.append(res.latency)
        suite_result_chart_data = json.dumps({
            'iops_list':iops_list,
            'latency_liat':latency_list
        })
    
    @staticmethod
    def _get_exe_list(context, argpost, plan_id, project):
        os_list = Spdk_Perf_Result.objects.filter(project_id=project)
        platform_list = Spdk_Perf_Result.objects.filter(project_id=project)
        os_id = argpost.get('os_id', None)
        platform_id = argpost.get('platform_id', None)

        exe_all = TestExecution.objects.filter(
            testplan_id=plan_id,
            project_id=project
        )
        exe_os = exe_platform = exe_all
        if platform_id:
            exe_platform = TestExecution.objects.filter(
                platform_id=platform_id,
                testplan_id=plan_id,
                project_id=project
            )
        if os_id:
            exe_os = TestExecution.objects.filter(
                os_id=os_id,
                testplan_id=plan_id,
                project_id=project
            )
        unordered_exe_all = list(set(exe_os) & set(exe_platform) & set(exe_all))
        exe_all = sorted(unordered_exe_all, key=operator.attrgetter('id'), reverse=True)

        exe_array = [(exe, PerfTestCaseResult.objects.filter(
            perf_testsuite_result__testexecution__id=exe.id).count()) for exe in exe_all]

        exe_page = int(argpost.get('execution_page', 1))
        exe_list, exe_page_range = paginator(exe_page, exe_array)

        context['exe_length'] = len(exe_all)
        context['exe_list'] = exe_list
        context['exe_page_range'] = exe_page_range
        context['os_list'] = os_list
        context['platform_list'] = platform_list

    @staticmethod
    def _get_suite_list(context, argpost, exe_id, project):
        suite_result_all = PerfTestSuiteResult.objects.filter(
            testexecution_id=exe_id,
            project_id=project
        )

        result_all = []
        for suite_result in suite_result_all:
            case_result_all = PerfTestCaseResult.objects.filter(perf_testsuite_result__id=suite_result.id)
            total = len(case_result_all)
            no_run_num = 0
            for case_result in case_result_all:
                detail_value_set = set(PerfTestCaseResultDetail.objects.filter(
                    perf_testcase_result__id=case_result.id).values_list('value'))

                if len(detail_value_set) == 1 and (None,) in detail_value_set:
                    no_run_num += 1
            run_num = total - no_run_num
            result_all.append((suite_result, total, run_num, no_run_num))

        suite_page = int(argpost.get('suite_page', 1))
        result_list, suite_page_range = paginator(suite_page, result_all)
        PerfRegularReportPlugin._get_suite_chart_data(context, result_all)

        context['suite_result_list'] = result_list
        context['suite_result_length'] = len(result_all)
        context['suite_page_range'] = suite_page_range

    @staticmethod
    def _get_suite_chart_data(context, suite_results):
        suite_name, pie_list, circle_list = [], [], []

        # suite_results data structure: ((suite_result, total, run_num, no_run_num))
        for res in suite_results:
            suite_result_obj = res[0]
            total_num = res[1]
            # if case number is 0 hide chart
            if total_num > 0:
                pie_list.append({
                    'value': total_num,
                    'name': suite_result_obj.testsuite.name
                    })
                suite_name.append(suite_result_obj.testsuite.name)

                circle_list.append({
                    'name': suite_result_obj.testsuite.name,
                    'run': res[2],
                    'no_run': res[3]
                    })

                context['suite_result_chart_data'] = json.dumps({
                    #'suite_name': suite_name,
                    #'pie_list': pie_list,
                    #'circle_list': circle_list
                    'pie_list': 'suite_results',
                    'circle_list': 'suite_results'

                })

    @staticmethod
    def _get_case_detail_result(context, suite_result_id, app_id, project_id, suite_detail_page):
        app_attr_list = AppAttr.objects.filter(
            app_id=app_id,
            project_id=project_id
        )
        testcase_result_list = PerfTestCaseResult.objects.filter(perf_testsuite_result_id=suite_result_id,
                                                                 project_id=project_id)
        detail_result_all = []
        for testcase_result in testcase_result_list:
            attr_result_list = []
            for attr in app_attr_list:
                try:
                    attr_result = PerfTestCaseResultDetail.objects.get(
                        perf_testcase_result_id=testcase_result.id,
                        key_id=attr.id
                    )
                    attr_result_list.append(attr_result.value)
                except PerfTestCaseResultDetail.DoesNotExist:
                    attr_result_list.append(None)

            detail_result_all.append((testcase_result, attr_result_list))

        detail_result_list, suite_detail_page_range = paginator(suite_detail_page, detail_result_all)

        context['app_attr_list'] = app_attr_list
        context['suite_detail_page_range'] = suite_detail_page_range
        context['detail_result_length'] = len(detail_result_all)
        context['detail_result_list'] = detail_result_list
        return detail_result_all

    @staticmethod
    def _get_case_result(suite_case_dict, exe_obj_list, appattr_obj_list):
        suite_result_dict = {}
        suite_case_result_dict = {}
        for suite in suite_case_dict.keys():
            for exe_obj in exe_obj_list:
                suite_result_obj = PerfTestSuiteResult.objects.get(testexecution=exe_obj, testsuite=suite)
                for case in suite_case_dict[suite]:
                    try:
                        caseresult_obj = PerfTestCaseResult.objects.get(testcase=case,perf_testsuite_result=suite_result_obj)
                    except ObjectDoesNotExist:
                        suite_result_dict[(case, suite, exe_obj)] = [None for attr in appattr_obj_list]
                        continue

                    if (suite.name, case.name) not in suite_case_result_dict:
                        suite_case_result_dict[(suite.name, case.name)] = [caseresult_obj.id]
                    else:
                        suite_case_result_dict[(suite.name, case.name)].append(caseresult_obj.id)

                    attr_result_list = []
                    for appattr in appattr_obj_list:
                        try:
                            caseresult_detail = PerfTestCaseResultDetail.objects.get(
                                perf_testcase_result=caseresult_obj, key=appattr)
                            try:
                                attr_result_list.append(float(caseresult_detail.value))
                            except AttributeError:
                                attr_result_list.append(None)
                            except TypeError:
                                attr_result_list.append(None)
                        except ObjectDoesNotExist:
                            attr_result_list.append(None)
                    suite_result_dict[(case, suite, exe_obj)] = attr_result_list
        return suite_result_dict, suite_case_result_dict

    @staticmethod
    def _get_diff_exe_result(context, exe_id_list):
        # get execution object list
        # Return ((suite, suite_count), (case, case_count), execution, result_list)
        exe_obj_list = []
        for exe_id in exe_id_list:
            exe_obj_list.append(TestExecution.objects.get(id=exe_id))

        appattr_obj_list = AppAttr.objects.filter(app=exe_obj_list[0].app).order_by('id')

        caseresult_dict = {}
        suite_case_dict = defaultdict(list)
        for exe_obj in exe_obj_list:
            suite_result_list = PerfTestSuiteResult.objects.filter(testexecution=exe_obj).order_by('id')
            for suite_result_obj in suite_result_list:
                caseresult_list = PerfTestCaseResult.objects.filter(perf_testsuite_result=suite_result_obj)
                for case_result in caseresult_list:
                    if case_result.testcase not in suite_case_dict[suite_result_obj.testsuite]:
                        suite_case_dict[suite_result_obj.testsuite].append(case_result.testcase)
                    result_detail_list = []
                    for attr in appattr_obj_list:
                        try:
                            value = PerfTestCaseResultDetail.objects.get(
                                perf_testcase_result=case_result,
                                key=attr
                            ).value
                        except PerfTestCaseResultDetail.DoesNotExist:
                            value = None
                        result_detail_list.append(value)
                    caseresult_dict[(suite_result_obj.testsuite,
                                     case_result.testcase,
                                     exe_obj)] = result_detail_list

        result_list = []
        for suite, case_list in suite_case_dict.items():
            suite_count = len(case_list) * len(exe_obj_list)
            for case in case_list:
                case_count = len(exe_obj_list)
                for exe_obj in exe_obj_list:
                    try:
                        detail_result = caseresult_dict[suite, case, exe_obj]
                    except KeyError:
                        detail_result = ['' for attr in appattr_obj_list]
                    result_list.append(((suite.name, suite_count), (case.name, case_count),
                                        exe_obj.name, detail_result))
                    case_count = 0
                    suite_count = 0
        print result_list

        title_list = ['suite', 'case', 'execution']
        for attr in appattr_obj_list:
            title_list.append(str(attr.name))

        context['exe_diff_result_list'] = result_list
        context['exe_diff_title_list'] = title_list

    @staticmethod
    def xxx(context, exe_id_list):
        exe_count = len(exe_id_list)
        exe_obj_list = []
        for exe_id in exe_id_list:
            exe_obj_list.append(TestExecution.objects.get(id=exe_id))
        # print 'exe_obj_list={0}'.format(exe_obj_list)

        testplan_obj = exe_obj_list[0].testplan
        # print 'testplan_obj={0}'.format(testplan_obj)

        appattr_obj_list = AppAttr.objects.filter(app=testplan_obj.app)
        # print 'appattr_obj_list={0}'.format(appattr_obj_list)

        testsuite_list = TestSuite.objects.filter(testplan=testplan_obj)
        # print 'testsuite_list={0}'.format(testsuite_list)

        suite_case_dict = {}
        for suite in testsuite_list:
            case_list = TestCase.objects.filter(testsuite=suite)
            suite_case_dict[suite] = case_list
        # print 'suite_case_dict={0}'.format(suite_case_dict)

        case_result_dict, suite_case_result_dict = PerfRegularReportPlugin._get_case_result(
            suite_case_dict, exe_obj_list, appattr_obj_list)
        # print case_result_dict
        result_list = []
        for suite in testsuite_list:
            suite_flag = True
            suite_count = len(suite_case_dict[suite]) * exe_count
            for case in suite_case_dict[suite]:
                case_count = len(exe_obj_list)
                exe_flag = True
                for exe_obj in exe_obj_list:
                    if exe_flag and suite_flag:
                        result_list.append(((suite.name, suite_count), (case.name, case_count),
                                           exe_obj.name, case_result_dict[(case, suite, exe_obj)]))
                        exe_flag = False
                        suite_flag = False
                    elif exe_flag:
                        result_list.append(((suite.name, None), (case.name, case_count),
                                           exe_obj.name, case_result_dict[(case, suite, exe_obj)]))
                        exe_flag = False
                    else:
                        result_list.append(((suite.name, None), (case.name, None), exe_obj.name,
                                            case_result_dict[case, suite, exe_obj]))

        title_list = ['suite', 'case', 'execution']
        for attr in appattr_obj_list:
            title_list.append(str(attr.name))
        print result_list
        context['exe_diff_result_list'] = result_list
        context['exe_diff_title_list'] = title_list
        context['suite_case_result_dict'] = suite_case_result_dict
        print suite_case_result_dict

    @staticmethod
    def _get_exe_chart_data(context, argpost, case_name, project):
        suite_name = argpost.get("selected_suite_name", None)
        exe_diff_result = argpost.get("exe_diff_result_list", None)

        if exe_diff_result:
            exe_diff_result_list = ast.literal_eval(exe_diff_result)
        else:
            print "exe_diff_result_list is empty"
            return

        exe_name_list, attr_name_list, chart_data_list = [], [], []

        # flag for chart_data_list, if chart has valid result 
        chart_data_flag = False

        # get attribute list
        app_id = TestCase.objects.get(
            name=case_name,
            project_id=project).app.id
        appattr_list = AppAttr.objects.filter(app_id=app_id)
        for appattr in appattr_list:
            attr_name_list.append(appattr.name)

    # exe_diff_result_list data structure: (((suite.name, suite_count), (case.name, case_count),
        #  exe_obj.name, detail_result))
        for res in exe_diff_result_list:
            value_list = []
            if res[0][0] == suite_name:
                if res[1][0] == case_name:

                    # flag for value_list , if exe has valid result
                    value_list_flag = False

                    for value in res[3]:
                        try:
                            value_list.append(float(value))
                            value_list_flag = True
                            chart_data_flag = True
                        except AttributeError:
                            value_list.append('-')
                        except TypeError:
                            value_list.append('-')
                        except ValueError:
                            value_list.append('-')

                    if value_list_flag:
                        exe_name_list.append(res[2])
                        chart_data_list.append(value_list)

        if chart_data_flag is False:
            chart_data_list = []

        context['case_chart_data'] = json.dumps({
            'attr_list': attr_name_list,
            'value_list': chart_data_list,
            'exe_list': exe_name_list
        })

    @staticmethod
    def _get_case_chart_data(context, detail_result_all, project):
        attr_list, attr_name_list, case_list, chart_data_list, result_list = [], [], [], [], []
        app_id = None
        for res in detail_result_all:
            case_result_obj = res[0]
            attr_value_list = res[1]

            # if case has valid result
            flag = False

            value_list = []
            for value in attr_value_list:
                try:
                    value_list.append(float(value))
                    flag = True
                except AttributeError:
                    value_list.append('-')
                except TypeError:
                    value_list.append('-')
                except ValueError:
                    value_list.append('-')

            if flag:
                case_list.append(case_result_obj.testcase.name)
                result_list.append(value_list)
                app_id = case_result_obj.testcase.app_id

        if app_id:
            # get attribute name list
            attr_list = AppAttr.objects.filter(app_id=app_id)
            for attr in attr_list:
                attr_name_list.append(attr.name)

            # matrix transpose
            chart_data_list = map(list,zip(*result_list))

            context['case_result_data'] = json.dumps({
                'attr_list': attr_name_list,
                'value_list': chart_data_list,
                'case_list': case_list
                })

    @staticmethod
    def _get_diff_suite_result(context, suite_id_list):
        suite_result_dict = {}
        key_list = []
        for suite_id in suite_id_list:
            attr_result_list = PerfTestCaseResultDetail.objects.filter(
                perf_testcase_result__perf_testsuite_result__testsuite_id=suite_id
            )
            result_dict = {}
            for r in attr_result_list:
                result_dict[(
                    r.perf_testcase_result.testcase.name,
                    r.key.name,
                    r.perf_testcase_result.testcase.id
                )] = r.value

                if (
                    r.perf_testcase_result.testcase.name,
                    r.key.name,
                    r.perf_testcase_result.testcase.id
                ) not in key_list:
                    key_list.append((
                        r.perf_testcase_result.testcase.name,
                        r.key.name,
                        r.perf_testcase_result.testcase.id
                    ))
            suite_result_dict[suite_id] = result_dict

        result_list = []
        for key in key_list:
            r_tmp_list = []
            for exe_id in suite_id_list:
                r_tmp_list.append(suite_result_dict[exe_id].get(key, None))
            r_list = list(set(r_tmp_list))
            if len(r_list) > 1:
                tmp_list = list(key) + r_tmp_list
                result_list.append(tmp_list)
        context['suite_diff_result_list'] = result_list

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = PerfRegularReportInfo.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        # view execution list
        plan_id = argget.get("plan_id", None)
        self._get_exe_list(context, argpost, plan_id, project.id)

        # view testsuite list
        exe_id = argpost.get("execution_id", None)
        if exe_id:
            self._get_suite_list(context, argpost, exe_id, project.id)

        # view testcase results
        suite_result_id = argpost.get("suite_result_id", None)
        app_id = argpost.get("app_id", None)
        suite_detail_page = int(argpost.get('suite_detail_page', 1))
        if suite_result_id and app_id:
            detail_result_all = self._get_case_detail_result(context, suite_result_id, app_id,
                                                             project.id, suite_detail_page)
        else:
            detail_result_all = None

        # compare execution
        selected_exe_id = argpost.get("selected_exe_id", None)
        if selected_exe_id:
            self._get_diff_exe_result(context, json.loads(selected_exe_id))

        # view testcase chart data
        if detail_result_all:
            self._get_case_chart_data(context, detail_result_all, project.id)

        # view execution result chart
        selected_case_name = argpost.get("selected_case_name", None)
        if selected_case_name:
            #self._get_exe_chart_data(context, argpost, selected_case_name, project.id)
            self._get_spdk_exe_result(context,argpost, selected_case_name, project.id)

        return context 


class PerfDPDKReportPlugin(CMSPluginBase):
    model = PerfDPDKReportInfo
    name = 'perf_DPDK_report_plugin'
    render_template = 'perf_DPDK_report_plugin.html'
    fields = ('title', 'size')


    @staticmethod
    def _get_spdk_exe_result(context,argpost,plan_id,project):
        result_list = Spdk_Perf_Result.objects.all()
        iops_list=[]
        latency_liat=[]
        for res in result_list:
            iops_list.append(res.iops)
            latency_liat.append(res.latency)
        context['iops_list']=iops_list
        context['latency_liat']=latency_liat

    @staticmethod
    def _get_dpdk_exe_list(context, argpost, plan_id, project):
        os_list = OS.objects.filter(project_id=project)
        platform_list = Platform.objects.filter(project_id=project)
        os_id = argpost.get('os_id', None)
        platform_id = argpost.get('platform_id', None)

        exe_all = TestExecution.objects.filter(
            testplan_id=plan_id,
            project_id=project
        )
        exe_os = exe_platform = exe_all
        if platform_id:
            exe_platform = TestExecution.objects.filter(
                platform_id=platform_id,
                testplan_id=plan_id,
                project_id=project
            )
        if os_id:
            exe_os = TestExecution.objects.filter(
                os_id=os_id,
                testplan_id=plan_id,
                project_id=project
            )
        unordered_exe_all = list(set(exe_os) & set(exe_platform) & set(exe_all))
        exe_all = sorted(unordered_exe_all, key=operator.attrgetter('id'), reverse=True)

        exe_array = [(exe, PerfDPDKTestCaseResult.objects.filter(
            perf_testsuite_result__testexecution__id=exe.id).count()) for exe in exe_all]

        exe_page = int(argpost.get('execution_page', 1))
        exe_list, exe_page_range = paginator(exe_page, exe_array)

        context['exe_length'] = len(exe_all)
        context['exe_list'] = exe_list
        context['exe_page_range'] = exe_page_range
        context['os_list'] = os_list
        context['platform_list'] = platform_list


    @staticmethod
    def _get_dpdk_suite_list(context, argpost, exe_id, project):
        suite_result_all = PerfTestSuiteResult.objects.filter(
            testexecution_id=exe_id,
            project_id=project
        )

        result_all = []
        for suite_result in suite_result_all:
            case_result_all = PerfDPDKTestCaseResult.objects.filter(perf_testsuite_result__id=suite_result.id)
            total = len(case_result_all)
            no_run_num = 0
            for case_result in case_result_all:
                detail_value_set = set(PerfDPDKTestCaseResultDetail.objects.filter(
                    perf_dpdk_testcase_result__id=case_result.id).values_list('value'))

                if len(detail_value_set) == 0:
                    no_run_num += 1
            run_num = total - no_run_num
            result_all.append((suite_result, total, run_num, no_run_num))

        suite_page = int(argpost.get('suite_page', 1))
        result_list, suite_page_range = paginator(suite_page, result_all)

        context['suite_result_list'] = result_list
        context['suite_result_length'] = len(result_all)
        context['suite_page_range'] = suite_page_range

    @staticmethod
    def _get_dpdk_case_result_detail(context, case_result_id, app_id, project_id):
        attr_name_list, attr_value_list, result_list, packet_size, chart_value_list = [], [], [], [], []

        # get attr name list
        attr_obj_list = AppAttr.objects.filter(
            app_id=app_id,
            project_id=project_id
        )

        # get attr_id for chart
        throughput_id = None
        packet_size_id = None
        for attr in attr_obj_list:
            attr_name_list.append(attr.name)
            if attr.name.lower() == "throughput(mpps)":
                throughput_id = attr.id
            if attr.name.lower() == "packet size(bytes)":
                packet_size_id = attr.id

        case_result = PerfDPDKTestCaseResultDetail.objects.filter(
            perf_dpdk_testcase_result__id=case_result_id
        ).order_by('group')

        if case_result:
            # group case result detail
            group_id = 1
            group_value_list, group_result_list = [], []
            for result in case_result:
                if result.group == group_id:
                    group_value_list.append(result)
                else:
                    group_result_list.append(group_value_list)
                    group_id = result.group
                    group_value_list = []
                    group_value_list.append(result)
            group_result_list.append(group_value_list)

            # get attr value for table
            for result in group_result_list:
                attr_value = []
                attr_value_flag = False
                for attr in attr_obj_list:
                    flag = False
                    for detail in result:
                        if detail.key_id == attr.id:
                            flag = True
                            try:
                                attr_value.append(detail.value)
                                attr_value_flag = True
                            except AttributeError:
                                attr_value.append(None)
                            except TypeError:
                                attr_value.append(None)
                            except ValueError:
                                attr_value.append(None)
                    if flag is False:
                        attr_value.append('')

                if attr_value_flag:
                    attr_value_list.append(attr_value)

            # get data for chart
            chart_value_list_flag = False
            for result in group_result_list:
                flag_value = False
                flag_packet = False
                for detail in result:
                    if detail.key_id == throughput_id:
                        flag_value = True
                        try:
                            chart_value_list.append(float(detail.value))
                            chart_value_list_flag = True
                        except AttributeError:
                            chart_value_list.append(None)
                        except TypeError:
                            chart_value_list.append(None)
                        except ValueError:
                            chart_value_list.append(None)
                    if detail.key_id == packet_size_id:
                        flag_packet = True
                        try:
                            packet_size.append(float(detail.value))
                        except AttributeError:
                            packet_size.append(None)
                        except TypeError:
                            packet_size.append(None)
                        except ValueError:
                            packet_size.append(None)
                if flag_packet is True and flag_value is False:
                    chart_value_list.append('_')

            if chart_value_list_flag is False:
                chart_value_list = []

            context['packet_size'] = packet_size
            context['chart_value_list'] = chart_value_list

        context['attr_obj_list'] = attr_obj_list
        context['result_list'] = attr_value_list


    @staticmethod
    def _get_dpdk_case_result(context, suite_result_id, app_id, project_id, suite_detail_page):

        dpdk_testcase_result_list = PerfDPDKTestCaseResult.objects.filter(perf_testsuite_result_id=suite_result_id,
                                                                 project_id=project_id)

        flag = False
        detail_result_all = []
        for testcase_result in dpdk_testcase_result_list:
            detail_value_set = PerfDPDKTestCaseResultDetail.objects.filter(
                perf_dpdk_testcase_result__id=testcase_result.id)
            if len(detail_value_set) > 0:
                flag = True
            detail_result_all.append(testcase_result)

        if flag is False:
            detail_result_all = []

        detail_result_list, suite_detail_page_range = paginator(suite_detail_page, detail_result_all)

        context['suite_detail_page_range'] = suite_detail_page_range
        context['detail_result_length'] = len(detail_result_all)
        context['detail_result_list'] = detail_result_list

    @staticmethod
    def _get_dpdk_diff_exe_result(context, exe_id_list):
        # get execution object list
        # Return ((suite, suite_count), (case, case_count), execution, result_list)
        exe_obj_list = []
        for exe_id in exe_id_list:
            exe_obj_list.append(TestExecution.objects.get(id=exe_id))

        appattr_obj_list = AppAttr.objects.filter(app=exe_obj_list[0].app).order_by('id')

        # get throughput and packetsize id
        throughput_id = None
        packet_size_id = None
        for attr in appattr_obj_list:
            if attr.name.lower() == "throughput(mpps)":
                throughput_id = attr.id
            if attr.name.lower() == "packet size(bytes)":
                packet_size_id = attr.id

        caseresult_dict = {}
        packet_size_all = []
        suite_case_dict = defaultdict(list)
        for exe_obj in exe_obj_list:
            suite_result_list = PerfTestSuiteResult.objects.filter(testexecution=exe_obj).order_by('id')
            for suite_result_obj in suite_result_list:
                caseresult_list = PerfDPDKTestCaseResult.objects.filter(perf_testsuite_result=suite_result_obj)
                for case_result in caseresult_list:
                    if case_result.testcase not in suite_case_dict[suite_result_obj.testsuite]:
                        suite_case_dict[suite_result_obj.testsuite].append(case_result.testcase)

                    # get packet_size detail obj
                    packet_size_detail_obj_list = PerfDPDKTestCaseResultDetail.objects.filter(
                        perf_dpdk_testcase_result=case_result,
                        key_id=packet_size_id
                    )

                    # get throughput detail obj
                    throughput_detail_obj_list = PerfDPDKTestCaseResultDetail.objects.filter(
                        perf_dpdk_testcase_result=case_result,
                        key_id=throughput_id
                    )
                    result_detail_list = []
                    for packet_size in packet_size_detail_obj_list:
                        for throughput in throughput_detail_obj_list:
                            if packet_size.group == throughput.group:
                                result_detail_list.append((packet_size.value, throughput.value))
                        if packet_size.value not in packet_size_all:
                            packet_size_all.append(packet_size.value)

                    caseresult_dict[(suite_result_obj.testsuite,
                                     case_result.testcase,
                                     exe_obj)] = result_detail_list

        result_list = []
        for suite, case_list in suite_case_dict.items():
            suite_count = len(case_list) * len(exe_obj_list)
            for case in case_list:
                case_count = len(exe_obj_list)
                for exe_obj in exe_obj_list:
                    detail_result = []
                    try:
                        result_value_list = caseresult_dict[suite, case, exe_obj]
                        for packet_size in packet_size_all:
                            flag = False
                            for detail in result_value_list:
                                if packet_size == detail[0]:
                                    detail_result.append(detail[1])
                                    flag = True
                            if flag is False:
                                detail_result.append('')
                    except KeyError:
                        detail_result = ['' for packet_size in packet_size_all]
                    result_list.append(((suite.name, suite_count), (case.name, case_count),
                                        exe_obj.name, detail_result))
                    case_count = 0
                    suite_count = 0

        title_list = ['suite', 'case', 'execution']
        for packet_size in packet_size_all:
            title_list.append(packet_size)

        context['dpdk_exe_diff_result_list'] = result_list
        context['dpdk_exe_diff_title_list'] = title_list
        context['packet_size_all'] = json.dumps(packet_size_all)


    @staticmethod
    def _get_dpdk_exe_chart_data(context, argpost, case_name, project):
        suite_name = argpost.get("selected_suite_name", None)
        dpdk_exe_diff_result = argpost.get("dpdk_exe_diff_result_list", None)

        if dpdk_exe_diff_result:
            dpdk_exe_diff_result_list = ast.literal_eval(dpdk_exe_diff_result)
        else:
            print "exe_diff_result_list is empty"
            return

        exe_name_list, attr_name_list, chart_data_list = [], [], []

        # flag for chart_data_list, if chart has valid result
        chart_data_flag = False

        # get attribute list
        app_id = TestCase.objects.get(
            name=case_name,
            project_id=project).app.id
        appattr_list = AppAttr.objects.filter(app_id=app_id)
        for appattr in appattr_list:
            attr_name_list.append(appattr.name)

# dpdk_exe_diff_result_list data structure:
        # (((suite.name, suite_count), (case.name, case_count), exe_obj.name, detail_result))
        for res in dpdk_exe_diff_result_list:
            value_list = []
            if res[0][0] == suite_name:
                if res[1][0] == case_name:

                    # flag for value_list , if exe has valid result
                    value_list_flag = False
                    for value in res[3]:
                        try:
                            value_list.append(float(value))
                            value_list_flag = True
                            chart_data_flag = True
                        except AttributeError:
                            value_list.append('-')
                        except TypeError:
                            value_list.append('-')
                        except ValueError:
                            value_list.append('-')

                    if value_list_flag:
                        exe_name_list.append(res[2])
                        chart_data_list.append(value_list)

        if chart_data_flag is False:
            chart_data_list = []

        context['case_chart_data'] = json.dumps({
            'attr_list': attr_name_list,
            'value_list': chart_data_list,
            'exe_list': exe_name_list
        })


    @check_login_required_flag
    def render(self, context, instance, placeholder):

        if not context['auth_flag']:
            return context

        config = PerfDPDKReportInfo.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )
        # view execution list
        plan_id = argget.get("plan_id", None)
        self._get_dpdk_exe_list(context, argpost, plan_id, project.id)


        # compare execution
        selected_exe_id = argpost.get("selected_exe_id", None)
        if selected_exe_id:
            self._get_dpdk_diff_exe_result(context, json.loads(selected_exe_id))
            #self._get_spdk_exe_result(context,json.loads(selected_exe_id))

        # view testsuite list
        exe_id = argpost.get("execution_id", None)
        if exe_id:
            #self._get_dpdk_suite_list(context, argpost, exe_id, project.id)
            self._get_spdk_exe_result(context,json.loads(execution_id))

        # view testcase results
        suite_result_id = argpost.get("suite_result_id", None)
        app_id = argpost.get("app_id", None)
        suite_detail_page = int(argpost.get('suite_detail_page', 1))
        if suite_result_id and app_id:
            self._get_dpdk_case_result(context, suite_result_id, app_id,
                                                             project.id, suite_detail_page)

        # view testcase detail result
        case_result_id = argpost.get("case_result_id", None)
        app_id = argpost.get("app_id", None)
        if case_result_id and app_id:
            self._get_dpdk_case_result_detail(context, case_result_id, app_id, project.id)

        # view execution result chart
        selected_case_name = argpost.get("selected_case_name", None)
        if selected_case_name:
            self._get_dpdk_exe_chart_data(context, argpost, selected_case_name, project.id)

        return context
    

class MyChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'my_chart_plugin'
    render_template = 'mydpdk_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)
        chart_data = None
        exec_list = TestExecution.objects.filter(testplan_id=plan_id,project_id=project.id)
        exe_array, throughput_array, lossrate_array, time_array = [], [], [], []
        for exe in exec_list:
            exe_array.append(exe.name)
            results = MySuiteResult.objects.filter(
                testexecution_id=exe.id,
                project_id=project.id
            )
        time_list = TestRecordTable.objects.filter(project_id = project.id)
        for time in time_list:
            time_array.append(time.create_time)
        throughput_list=MySuiteResult.objects.filter(project_id=project.id)
        for thr in throughput_list:
            throughput_array.append(thr.zero_loss_throughput)
            lossrate_array.append(thr.zero_loss_rate)

        if len(exec_list) > 0:
            chart_data = json.dumps({
                'exe_array': exe_array,
                'exec_length': len(exec_list),
                #'rate_array': rate_array,
                'throughput_array': throughput_array,
                'lossrate_array': lossrate_array
                #'time_array':time_array
            })

        context['chart_data'] = chart_data
        context['exec_list'] = exec_list
        #context['plan_id'] = time_array
        context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        return context

################ NEW UI#########################
class UiChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'ui_chart_plugin'
    render_template = 'ui_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)
        chart_data = None
        exec_list = TestExecution.objects.filter(testplan_id=plan_id,project_id=project.id)
        exe_array, throughput_array, lossrate_array, time_array = [], [], [], []
        for exe in exec_list:
            exe_array.append(exe.name)
            results = MySuiteResult.objects.filter(
                testexecution_id=exe.id,
                project_id=project.id
            )
        time_list = TestRecordTable.objects.filter(project_id = project.id)
        for time in time_list:
            time_array.append(time.create_time)
        throughput_list=MySuiteResult.objects.filter(project_id=project.id)
        for thr in throughput_list:
            throughput_array.append(thr.zero_loss_throughput)
            lossrate_array.append(thr.zero_loss_rate)

        if len(exec_list) > 0:
            chart_data = json.dumps({
                'exe_array': exe_array,
                'exec_length': len(exec_list),
                #'rate_array': rate_array,
                'throughput_array': throughput_array,
                'lossrate_array': lossrate_array
                #'time_array':time_array
            })

        context['chart_data'] = chart_data
        context['exec_list'] = exec_list
        context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        return context



class MyTimeChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'mytime_chart_plugin'
    render_template = 'mytime_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context
			
        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size
        project = Project.objects.get(name=context['request'].session['project'])

        chart_data = None
        time_list = TimeRecordTable.objects.filter(project_id=project.id)
        frame_size_array ,throughput_array, sendrate_array, time_list = [], [], [],[]
        for time in time_list:
            time_array.append(time.create_time)
        frame_size_list = NicPerfTable.objects.filter(project_id = project.id)
        for frame in frame_size_list:
            frame_size_array.append(frame.frame_size)
        throughput_list=NicPerfTable.objects.filter(project_id = project.id)
        for thr in throughput_list:
            throughput_array.append(thr.throughput)
        sendrate_list=NicPerfTable.objects.filter(project_id= project.id)
        for sendrate in sendrate_list:
            sendrate_array.append(sendrate.send_rate)
    	if len(time_list) > 0:
		chart_data = json.dumps({
		'time_array': time_array,
        'frame_size_array': frame_size_array,
        'throughput_array': throughput_array,
        'send_rate_array': sendrate_array
        })

    	context['chart_data'] = chart_data
    	context['exec_list'] = exec_list
        return context 

class SpdkChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'spdk_perf_chart_plugin'
    render_template = 'spdk_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)
        exe_id = argpost.get("exe_id",None)
        rw_id =argpost.get("rw_id",None)
        if rw_id:
            exec_list = TestExecution.objects.filter(
                        rw_id=rw_id,
                        testplan_id=plan_id,
                        project_id=project.id
                    )
        else:
            exec_list = TestExecution.objects.filter(testplan_id=plan_id,rw_id=1,project_id=project.id)
        chart_data = None
        exe_array,time_array,iops_array,latency_array,result_iops,rw_array,io_size_array =[],[],[],[],[],[],[] 
        #exec_list = TestExecution.objects.filter(testplan_id=plan_id,project_id=project.id)
        for exe in exec_list:
            exe_array.append(exe.name)
            results = Spdk_Perf_Result.objects.filter(
                testexecution_id=exe.id,
            )
            for res in results:
                iops_array.append(res.iops)
                latency_array.append(res.latency)
        time_list = Spdk_Perf_Result.objects.filter(project_id=project.id)
        rw_list =Rw_method.objects.filter(project_id=project.id)
        #io_size_list = io_size.objects.filter(project_id=project.id)
        for time in time_list:
            time_array.append(time.create_time)
        #iops_list=Spdk_Perf_Result.objects.filter(testexecution_id=exe_id)
        for rw in rw_list:
            rw_array.append(rw.rw_method)
        #for io_size in io_size_list:
        #    io_size_array.append(io_size.io_size)
        if len(exec_list)>0:
            chart_data = json.dumps({
                'exe_array':exe_array,
                'exec_length':len(exec_list),
                'iops_array': iops_array,
                'latency_array': latency_array,
                'time_array':'time_array',
                'rw_array':rw_array,
                #'io_size_array':io_size_array,

            })        
        context['chart_data'] = chart_data
        context['rw_list']= rw_list
        context['exec_list']= exec_list
        #context['io_size_list']= io_size_list
        #context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        return context 


class SpdkTrendChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'spdk_trend_chart_plugin'
    render_template = 'spdk_trend_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )
        rw_id =argpost.get("rw_id", None)
        platform_id = argpost.get("platform_id",None)
        plan_id = argget.get("plan_id", None)
        '''
        if rw_id:
            result_list = SpdkAvgTrendTable.objects.filter(
            rw_method_id = rw_id,
            #project_id=project.id
            )
        else:
            result_list = SpdkAvgTrendTable.objects.filter(rw_method=1)
        if platform_id:
            platform_plan = SpdkAvgTrendTable.objects.filter(queue_depth_id=queue_depth_id)
        else:
            platform_plan = SpdkAvgTrendTable.objects.filter(queue_depth_id=1)
        '''
#################### 
        if rw_id and platform_id:
            result_list = SpdkAvgTrendTable.objects.filter(
                rw_method_id=rw_id,
                queue_depth=platform_id,
                #testplan_id=plan_id,
                project_id=project.id
            )
        elif rw_id:
            result_list = SpdkAvgTrendTable.objects.filter(
                rw_method_id=rw_id,
                #testplan_id=plan_id,
                project_id=project.id
            )
        elif platform_id:
            result_list = SpdkAvgTrendTable.objects.filter(
                queue_depth=platform_id,
                #testplan_id=plan_id,
                project_id=project.id
            )
        else:
            result_list = SpdkAvgTrendTable.objects.filter(
                #testplan_id=plan_id,
                rw_method_id=1,
                queue_depth=1
                #project_id=project.id
            )
        chart_data = None
        exe_array,time_array,iops_array,latency_array = [],[],[],[] 
        ############
        commit_info_list = TestRecordTable.objects.all() 
        #for exe in exec_list:
        #    exe_array.append(exe.name)
        #    results = MySuiteResult.objects.filter(
        #        testexecution_id=exe.id,
        #        project_id=project.id
        #    )
        #time_list = SpdkAvgTrendTable.objects.all()
        #time_list = Spdk_Perf_Result.objects.all()
        #for time in time_list:
        #    create_time = time.create_time.strftime("%y-%m-%d")
        #    time_array.append(str(create_time))
        #iops_list=Spdk_Perf_Result.objects.filter(project_id=project.id)
        iops_list=Spdk_Perf_Result.objects.all()
        for res in result_list:
            iops_array.append(res.trend_iops)
            latency_array.append(res.trend_latency)
            time_array.append(str(res.create_time.strftime("%y-%m-%d")))
        queue_depth_list= Queue_depth.objects.all()
        rw_method_list= Rw_method.objects.filter(project_id=project.id)
        if len(result_list)>0:
            chart_data = json.dumps({
                'iops_array': iops_array,
                'latency_array': latency_array,
                'time_array': time_array
            })
        
        context['chart_data'] = chart_data
        #context['time_array']= time_array
        #########
        context['commit_info_list']=commit_info_list
        #context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        context['queue_depth_list'] = queue_depth_list
        context['rw_list'] = rw_method_list
        return context

class DpdkTrendChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'dpdk_trend_chart_plugin'
    render_template = 'dpdk_trend_chart_plugin.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        #plan_id = argget.get("plan_id", None)
        chart_data = None
        exe_array,time_array,throughput_array,send_rate_array = [],[],[],[] 
        exec_list = TestExecution.objects.all()
        ############
        commit_info_list=TestRecordTable.objects.all() 
        for exe in exec_list:
            exe_array.append(exe.name)
            results = MySuiteResult.objects.filter(
                testexecution_id=exe.id,
                project_id=project.id
            )
        time_list = NicPerfTable.objects.all()
        #time_list = Spdk_Perf_Result.objects.all()
        for time in time_list:
            create_time=time.create_time.strftime("%Y-%m-%d")
            time_array.append(str(create_time))
        #iops_list=Spdk_Perf_Result.objects.filter(project_id=project.id)
        throughput_list=NicPerfTable.objects.all()
        for throughput in throughput_list:
            throughput_array.append(throughput.thoughput)
            send_rate_array.append(throughput.send_rate)
        if len(exec_list)>0:
            chart_data = json.dumps({
                'throughput_array': throughput_array,
                'send_rate_array': send_rate_array,
                'time_array': time_array,
            })
        
        context['chart_data'] = chart_data
        #context['time_list']= time_list
        #########
        context['commit_info_list']=commit_info_list
        #context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        return context 

class SpdkDetailChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'spdk_detail_chart_plugin'
    render_template = 'spdk_detail.html'
    fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

        config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
        size = get_config_size(config.size)
        context['title'] = config.title
        context['size'] = size

        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )

        plan_id = argget.get("plan_id", None)
        exe_id = argget.get("execution_id",None)
        rw_id =argpost.get("rw_id",None)
        if rw_id:
            exec_list = TestExecution.objects.filter(
                        rw_id=rw_id,
                        testplan_id=plan_id,
                        project_id=project.id
                    )
        else:
            #exec_list = TestExecution.objects.filter(id=exe_id,project_id=project.id)
            #exec_list = TestExecution.objects.filter(id=exe_id,project_id=project.id)
            plan_list = TestExecution.objects.filter(id=exe_id)
			#from from get exe_id and filter exe_obj:
            exec_list1 = TestExecution.objects.filter(id=exe_id,project_id=project.id)
			#get find the plan_id according exec_list1:
            plan_id_list=[]
            for exe in exec_list1:
                plan_id_list.append(exe.testplan)

            plan_id=plan_id_list[0]
			#Get All exec in One Testplan: 
            exec_list = TestExecution.objects.filter(testplan=plan_id,project_id=project.id)

            #exec_list = TestExecution.objects.all()
        chart_data = None
        exe_array,time_array,iops_array,latency_array,result_iops,rw_array,io_size_array =[],[],[],[],[],[],[] 
        #exec_list = TestExecution.objects.filter(testplan_id=plan_id,project_id=project.id)
		#
        for exe in exec_list:
            exe_array.append(exe.rw.rw_method)  
            results = Spdk_Perf_Result.objects.filter(
                testexecution_id=exe.id,
            )
            for res in results:
                #exe_array.append(res.rw_method.rw_method)
                iops_array.append(res.iops)
                latency_array.append(res.latency)
        time_list = Spdk_Perf_Result.objects.filter(project_id=project.id)
        rw_list =Rw_method.objects.filter(project_id=project.id)
        #io_size_list = io_size.objects.filter(project_id=project.id)
        for time in time_list:
            time_array.append(time.create_time)
        #iops_list=Spdk_Perf_Result.objects.filter(testexecution_id=exe_id)
        for rw in rw_list:
            rw_array.append(rw.rw_method)
        #for io_size in io_size_list:
        #    io_size_array.append(io_size.io_size)
        rw_type_list=Rw_method.objects.filter(project_id=project.id)
        rw_type_array=[]
        for rw_type in rw_type_list:
            rw_type_array.append(rw_type.rw_method)
        if len(exec_list)>0:
            chart_data = json.dumps({
                'exe_array':exe_array,
                'exec_length':len(exec_list),
                'iops_array': iops_array,
                'latency_array': latency_array,
                'time_array':'time_array',
                'rw_array':rw_array,
                'rw_type_array':rw_type_array
                #'io_size_array':io_size_array,

            })        
        context['chart_data'] = chart_data
        context['rw_list']= rw_list
        context['exec_list']= exec_list
        #context['io_size_list']= io_size_list
        #context['plan_id'] = time_array
        #context['throughput_list'] = throughput_list
        return context 
plugin_pool.register_plugin(RegularReportChartPlugin)
plugin_pool.register_plugin(RegularReportPlugin)
plugin_pool.register_plugin(TestplanReportPlugin)
plugin_pool.register_plugin(NicTestplanReportPlugin)
plugin_pool.register_plugin(PerfRegularReportPlugin)
plugin_pool.register_plugin(PerfDPDKReportPlugin)
plugin_pool.register_plugin(MyChartPlugin)
plugin_pool.register_plugin(UiChartPlugin)
plugin_pool.register_plugin(MyTimeChartPlugin)
plugin_pool.register_plugin(SpdkTestplanReportPlugin)
plugin_pool.register_plugin(SpdkChartPlugin)
plugin_pool.register_plugin(SpdkTrendChartPlugin)
plugin_pool.register_plugin(DpdkTrendChartPlugin)
plugin_pool.register_plugin(SpdkDetailChartPlugin)


