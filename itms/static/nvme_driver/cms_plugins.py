from __future__ import division
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.http import QueryDict
from plugins.nvme_driver.models import *
from base_models.models import *
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from utils.decorators import check_login_required_flag
import operator
import json
import operator
import ast
from collections import defaultdict
import time


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

class NvmeDriverTrendChartPlugin(CMSPluginBase):
    #model = RegularReportChart
    name = 'nvme_driver_trend_chart_plugin'
    render_template = 'nvme_driver.html'
    #fields = ('title', 'size')

    @check_login_required_flag
    def render(self, context, instance, placeholder):
        if not context['auth_flag']:
            return context

    #    config = RegularReportChart.objects.get(cmsplugin_ptr_id=instance)
    #    size = get_config_size(config.size)
    #    context['title'] = config.title
    #    context['size'] = size
        argpost = QueryDict.dict(context['request'].POST)
        argget = QueryDict.dict(context['request'].GET)
        project = Project.objects.get(
            name=context['request'].session['project']
        )
        rw_id =argpost.get("rw_id", None)
        platform_id = argpost.get("platform_id",None)
        plan_id = argget.get("plan_id", None)
#################### 
        if rw_id and queue_depth_id:
            result_list = NvmeDriverTrendTable.objects.filter(
                rw_method_id=rw_id,
                queue_depth=platform_id,
            )
        elif rw_id:
            result_list = NvmeDriverTrendTable.objects.filter(
                rw_method_id=rw_id,
            )
        elif platform_id:
            result_list = NvmeDriverTrendTable.objects.filter(
                queue_depth=platform_id,
            )
        else:
            result_list = NvmeDriverTrendTable.objects.filter(
                rw_method_id=1,
                #queue_depth=1
            )
        chart_data = None
        exe_array,time_array,iops_array,latency_array = [],[],[],[] 
        ############
        commit_info_list = TestRecordTable.objects.all() 
        for res in result_list:
            iops_array.append(res.trend_iops)
            latency_array.append(res.trend_latency)
            time_array.append(str(res.create_time.strftime("%y-%m-%d")))
        queue_depth_list= Queue_depth.objects.all()
        rw_method_list= Rw_method.objects.filter(project_id=project.id)
        workload_mix = NvmeDriverTrendTable.objects.distinct().values("workload_mix") 
        core_mask_list = NvmeDriverTrendTable.objects.distinct().values("Core_Mask") 
	io_size_list = io_size.objects.all()
        if len(result_list)>0:
            chart_data = json.dumps({
                'iops_array': iops_array,
                'latency_array': latency_array[-7:],
                'time_array': time_array[-7:],
                #'commit_info_list':commit_info_list
            })
        
        context['chart_data'] = chart_data
        context['commit_info_list']=commit_info_list
        context['queue_depth_list'] = queue_depth_list
        context['rw_list'] = rw_method_list
	context['io_size_list'] = io_size_list
	context['workload_mix'] = workload_mix
	context['core_mask_list'] = core_mask_list
        return context
  
    
plugin_pool.register_plugin(NvmeDriverTrendChartPlugin)
    
    
