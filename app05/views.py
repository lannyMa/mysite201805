from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import json


# Create your views here.


def index(request):
    return HttpResponse("index page")

