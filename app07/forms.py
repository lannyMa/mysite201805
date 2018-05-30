#!/usr/bin/env python
# coding=utf-8

from django.forms import ModelForm
from app07.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
