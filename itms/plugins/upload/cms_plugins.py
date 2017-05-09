from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plugins.upload.models import *
import os


class UploadPlugin(CMSPluginBase):
    model = UploadInfo
    name = 'upload_plugin'
    render_template = 'upload_plugin.html'

    def handle_uploaded_file(self, f, instance):
        config = UploadInfo.objects.get(cmsplugin_ptr_id=instance)
        path = config.path
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            file_name = path + f.name
            destination = open(file_name, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
            return 'Success'
        except Exception, e:
            print e
            return e

    def upload_file(self, request, instance):
        status = ''
        if request.method == 'POST':
            print request.method
            files = request.FILES.getlist('file')
            print len(files)
            for f in files:
                status = self.handle_uploaded_file(f, instance)
                print f.name
        return status

    def render(self, context, instance, placeholder):
        context['upload_status'] = self.upload_file(context['request'], instance)

        return context

plugin_pool.register_plugin(UploadPlugin)
