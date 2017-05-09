from django.db import models
from cms.models.pluginmodel import CMSPlugin


class ExeInfo(CMSPlugin):
    path = models.CharField(max_length=200, help_text='Example: media/files/')
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


class iTECInfo(CMSPlugin):
    title = models.CharField(max_length=50, default=None)
    size = models.CharField(max_length=20, help_text='Example: height*width')


