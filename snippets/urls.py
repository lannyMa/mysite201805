#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from django.conf.urls import url
from snippets import views

app_name = 'snippets'
urlpatterns = [
    # path('', views.index, name="index"),
    path('snippets', views.SnippetList.as_view(), name="snippets"),
]
