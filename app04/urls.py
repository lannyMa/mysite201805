#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from app04 import views


# 测试json
app_name = 'app04'
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('home2/', views.home2, name="home2"),
]
