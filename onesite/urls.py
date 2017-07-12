# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from onesite.views import *

urlpatterns = patterns('',
    url(r'^$', one_site_demo),
    url(r'^all/$', one_site_all),
    url(r'^last/$', one_site_last_record),
)
