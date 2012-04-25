from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', {"template": "index.html"}, name="index"),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

    (r'^doc/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.DOC_ROOT
    }),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
