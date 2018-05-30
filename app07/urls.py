#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from django.conf.urls import url
from app07 import views

app_name = 'app07'
urlpatterns = [
    path('', views.index, name="index"),
]
