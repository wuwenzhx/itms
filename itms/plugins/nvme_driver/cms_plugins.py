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
        queue_depth_id = argpost.get("queue_depth_id",None)
        #platform_id = argpost.get("platform_id",None)
        rw_id =argpost.get("rw_id", None)
        core_mask =argpost.get("core_mask", None)
        #io_size = argpost.get("io_size", None)
        #workload_mix = argpost.get("workload_mix", None)
        plan_id = argget.get("plan_id", None)

#################### 
        if rw_id and queue_depth_id:
            result_list = NvmeDriverTrendTable.objects.filter(
                rw_method_id=rw_id,
                queue_depth_id=queue_depth_id,
            )
        elif rw_id:
            result_list = NvmeDriverTrendTable.objects.filter(
                rw_method_id=rw_id,
            )
        elif queue_depth_id:
            result_list = NvmeDriverTrendTable.objects.filter(
                queue_depth_id=queue_depth_id,
                #rw_method_id=6,
            )
        else:
            result_list = NvmeDriverTrendTable.objects.filter(
                rw_method_id=6,
                #queue_depth_id = queue_depth_id,
            )
        if core_mask and 
        #if queue_depth_id:
        #    result_list = NvmeDriverTrendTable.objects.filter(queue_depth_id = queue_depth_id)
        chart_data = None
        exe_array,time_array,iops_array,latency_array,MBps_array,Min_lat_array,Max_lat_array=[],[],[],[],[],[],[] 
        ############
        #commit_info_list = TestRecordTable.objects.all() 
        for res in result_list:
            iops_array.append(res.trend_iops)
            latency_array.append(res.trend_latency)
            time_array.append(str(res.create_time.strftime("%y-%m-%d")))
            MBps_array.append(res.MBps)
            Min_lat_array.append(res.Min_lat)
            Max_lat_array.append(res.Max_lat)
        queue_depth_list= Queue_depth.objects.filter(project_id = project.id)
        rw_method_list= Rw_method.objects.filter(project_id=project.id)
        workload_mix_list = NvmeDriverTrendTable.objects.distinct().values("workload_mix") 
        core_mask_list = NvmeDriverTrendTable.objects.distinct().values("Core_Mask")
        io_size_list = io_size.objects.all()
        if len(result_list)>0:
            chart_data = json.dumps({
                'iops_array': iops_array[-7:],
                'latency_array': latency_array[-7:],
                'time_array': time_array[-7:],
                #'commit_info_list':commit_info_list
                'MBps_array':MBps_array[-7:],
                'Min_lat_array':Min_lat_array[-7:],
                'Max_lat_array':Max_lat_array[-7:],
                'queue_depth_id': queue_depth_id,
                'rw_id':rw_id,
                'core_mask':core_mask,
                #'io_size':io_size,
                #'workload_mix':workload_mix.workload_mix
            })
        
        context['chart_data'] = chart_data
        #context['commit_info_list']=commit_info_list
        context['queue_depth_list'] = queue_depth_list
        context['rw_list'] = rw_method_list
	context['io_size_list'] = io_size_list
	context['workload_mix_list'] = workload_mix_list
	context['core_mask_list'] = core_mask_list
        return context
  
    
plugin_pool.register_plugin(NvmeDriverTrendChartPlugin)
    
    
