# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from onesite.views import *

urlpatterns = patterns('',
    url(r'^$', one_site_all),
)
