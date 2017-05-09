from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.

class UploadInfo(CMSPlugin):
    path = models.CharField(max_length=100, help_text='Example: media/files/')

