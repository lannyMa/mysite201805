#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetList)

app_name = 'snippets'
urlpatterns = [
    path('', include(router.urls))
]
