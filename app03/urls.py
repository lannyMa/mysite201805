#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from app03 import views

app_name = 'app03'
urlpatterns = [
    path('addbook/', views.addbook, name="addbook"),
]
