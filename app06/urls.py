#!/usr/bin/env python
# coding=utf-8

from django.urls import path, include
from django.conf.urls import url
from app06 import views
from app06 import views_base

app_name = 'app06'
urlpatterns = [
    # path('', views.index, name="index"),
    # path('1/', views_base.ArticleView1.as_view(), name="ArticleView1"),
    # path('2/', views_base.ArticleView2.as_view(), name="ArticleView2"),
    path('3/', views_base.ArticlesView3.as_view(), name="ArticleView3"),
    path('articles/', views.ArticlesListView.as_view(), name="ArticlesListView"),

    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
]
