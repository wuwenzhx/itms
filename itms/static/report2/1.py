
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
from cms_plugin import  UndatedReportPlugin


render(self,context,instance,placeholder) 
