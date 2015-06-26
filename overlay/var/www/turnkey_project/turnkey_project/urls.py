from django.conf.urls import patterns, include, url
from django.contrib import admin
from turnkey_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turnkey_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
