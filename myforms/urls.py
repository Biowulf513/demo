# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from myforms.views import *


urlpatterns = patterns('',
    url(r'^$', my_name),
)
