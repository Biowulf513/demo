# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from info.views import info

urlpatterns = patterns('',
    url(r'^$', info),
                       )