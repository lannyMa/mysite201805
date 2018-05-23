#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from app05 import views

app_name = 'app05'
urlpatterns = [
    path('', views.index, name="index"),
]
