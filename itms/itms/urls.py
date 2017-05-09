from django.conf.urls import *
from django.contrib import admin


from django.template.loader import add_to_builtins

add_to_builtins('cms.templatetags.cms_tags')
add_to_builtins('sekizai.templatetags.sekizai_tags')
add_to_builtins('django.templatetags.static')
# add_to_builtins('pagination.templatetags.pagination_tags')
add_to_builtins('menus.templatetags.menu_tags')

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include('restapi.urls')),
                       url(r'^', include('cms.urls')),
                       )
