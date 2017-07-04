from django.conf.urls import patterns, include, url
from django.contrib import admin
from info.views import index

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^onesite/', include('onesite.urls'), name='onesite'),
    url(r'^info/', include('info.urls'), name='info'),
    url(r'^$', index ),
)
