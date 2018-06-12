#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from app02 import views

# 测试模型
app_name = 'app02'
urlpatterns = [
    path('addbook/', views.addbook, name="addbook"),
    path('addbook2/', views.addbook2, name="addbook2"),
    path('home/', views.home, name="home"),
]
