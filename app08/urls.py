#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from django.conf.urls import url
from app08 import views

app_name = 'app08'
urlpatterns = [
    path('', views.index, name="index"),
    path('add_ask', views.AddUserAskView.as_view() , name="add_ask"),
]
