from __future__ import division
from cms.plugin_base import CMSPluginBase
from django.core.exceptions import ObjectDoesNotExist
from cms.plugin_pool import plugin_pool
from django.http import QueryDict
from plugins.VhostScsi.models import *
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



class Vhost_Scsi_Trend_ChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'vhost_scsi_trend_chart_plugin'
    render_template = 'vhost_scsi_trend_plugin.html'
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

        if rw_id and platform_id:
            result_list = Vhost_Scsi_Trend_Table.objects.filter(
                rw_method_id=rw_id,
                queue_depth=platform_id,
            )
        elif rw_id:
            result_list = Vhost_Scsi_Trend_Table.objects.filter(
                rw_method_id=rw_id,
            )
        elif platform_id:
            result_list = Vhost_Scsi_Trend_Table.objects.filter(
                queue_depth=platform_id,
            )
        else:
            result_list = Vhost_Scsi_Trend_Table.objects.filter(
                rw_method_id=1,
                queue_depth=1
            )
        chart_data = None
        exe_array,time_array,iops_array,latency_array = [],[],[],[] 
        commit_info_list = TestRecordTable.objects.all() 
        iops_list=Vhost_Scsi_Perf_Result.objects.all()
        for res in result_list:
            iops_array.append(res.trend_iops)
            latency_array.append(res.trend_latency)
            time_array.append(str(res.create_time.strftime("%y-%m-%d")))
        queue_depth_list= Queue_depth.objects.all()
        rw_method_list= Rw_method.objects.filter(project_id=project.id)
        if len(result_list)>0:
            chart_data = json.dumps({
                'iops_array': iops_array[-7:],
                'latency_array': latency_array[-7:],
                'time_array': time_array[-7:]
            })
        
        context['chart_data'] = chart_data
        context['commit_info_list']=commit_info_list
        context['queue_depth_list'] = queue_depth_list
        context['rw_list'] = rw_method_list
        return context

class Vhost_Scsi_Detail_ChartPlugin(CMSPluginBase):
    model = RegularReportChart
    name = 'vhost_scsi_detail_chart_plugin'
    render_template = 'vhost_scsi_detail.html'
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
            plan_list = TestExecution.objects.filter(id=exe_id)
            exec_list1 = TestExecution.objects.filter(id=exe_id,project_id=project.id)
            plan_id_list=[]
            for exe in exec_list1:
                plan_id_list.append(exe.testplan)

            plan_id=plan_id_list[0]
	    #Get All exec in One Testplan: 
            exec_list = TestExecution.objects.filter(testplan=plan_id,project_id=project.id)

        chart_data = None
        exe_array,time_array,iops_array,latency_array,result_iops,rw_array,io_size_array =[],[],[],[],[],[],[] 
        for exe in exec_list:
            exe_array.append(exe.rw.rw_method)  
            results = Vhost_Scsi_Perf_Result.objects.filter(
                testexecution_id=exe.id,
            )
            for res in results:
                #exe_array.append(res.rw_method.rw_method)
                iops_array.append(res.iops)
                latency_array.append(res.latency)
        time_list = Vhost_Scsi_Perf_Result.objects.filter(project_id=project.id)
        rw_list =Rw_method.objects.filter(project_id=project.id)
        for time in time_list:
            time_array.append(time.create_time)
        for rw in rw_list:
            rw_array.append(rw.rw_method)
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

            })        
        context['chart_data'] = chart_data
        context['rw_list']= rw_list
        context['exec_list']= exec_list
        return context 


plugin_pool.register_plugin(Vhost_Scsi_Trend_ChartPlugin)
plugin_pool.register_plugin(Vhost_Scsi_Detail_ChartPlugin)
