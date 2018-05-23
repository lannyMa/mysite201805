#!/usr/bin/env python
# coding=utf-8
from django.http import HttpResponse, JsonResponse

from app06.models import Articles
from django.views.generic import View


class ArticlesView1(View):
    def get(self, request):
        # 从库中去数据 --> dict --> josn化返回
        all_Articles = Articles.objects.all()
        json_list = []
        for post in all_Articles:
            json_dict = {}
            json_dict['title'] = post.title
            json_dict['content'] = post.content
            json_list.append(json_dict)
        import json
        return HttpResponse(json.dumps(json_list), content_type="application/json")


class ArticlesView2(View):
    def get(self, request):
        all_aritcle = Articles.objects.all()
        json_list = []
        from django.forms.models import model_to_dict
        for aritcle in all_aritcle:
            json_dict = model_to_dict(aritcle)
            json_list.append(json_dict)
        return JsonResponse(json_list, safe=True)


class ArticlesView3(View):
    def get(self, request):
        all_Articles = Articles.objects.all()
        from django.core import serializers
        json_data = serializers.serialize('json', all_Articles)
        print(json_data)
        print(type(json_data))
        # return HttpResponse(json_data, content_type='application/json')
        import json
        json_list = json.loads(json_data)
        return JsonResponse(json_list, safe=False)
