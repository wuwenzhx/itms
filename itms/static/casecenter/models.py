from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.
class RequirementInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class FeatureInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class TestCaseInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class TestSuiteInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class TestPlanInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class AppInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')
