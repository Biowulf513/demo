# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', info),
    url(r'^music/', view_music),
    url(r'^group/', view_group),
    url(r'^friend/', view_friend),
    url(r'^note/', view_note),
)