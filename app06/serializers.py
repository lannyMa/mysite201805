#!/usr/bin/env python
# coding=utf-8

from rest_framework import serializers


class ArticlesSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    content = serializers.CharField(required=True)
    click_nums = serializers.IntegerField(default=0)
    add_time = serializers.DateTimeField(allow_null=True)
    # image = serializers.ImageField(allow_null=True)
