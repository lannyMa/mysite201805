#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from app01 import views


# 测试后台
app_name = 'app01'
urlpatterns = [
    path('', views.index, name="index"),
]
