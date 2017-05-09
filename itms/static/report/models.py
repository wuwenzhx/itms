from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.
class RegularReportChart(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class RegularReportInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class UndatedReportChart(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class UndatedReportInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class PerfRegularReportInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class PerfRegularReportInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class PerfDPDKReportInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')
