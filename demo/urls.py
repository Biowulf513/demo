from django.conf.urls import patterns, include, url
from django.contrib import admin
from info.views import index

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^onesite/', include('onesite.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^forms/', include('myforms.urls')),

    url(r'^$', index ),
)
