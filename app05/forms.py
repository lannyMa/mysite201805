#!/usr/bin/env python
# coding=utf-8

from django import forms


class UserInfo(forms.Form):
    email = forms.EmailField(required=True)
