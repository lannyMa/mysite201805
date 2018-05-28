#!/usr/bin/env python
# coding=utf-8
from django.http import HttpResponse, JsonResponse

from app06.models import Articles
from django.views.generic import View


class ArticlesView1(View):
    def get(self, request):
        # 从库中去数据 --> dict --> josn化返回
        # 手动转换dict
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
    '''
    HttpResponse用JsonResponse取代
    使用model_to_dict方法
    '''

    def get(self, request):
        all_article = Articles.objects.all()
        json_list = []
        from django.forms.models import model_to_dict
        for article in all_article:
            json_dict = model_to_dict(article)  # 缺点,不能对datatimefiled和imagefiled的model序列化
            json_list.append(json_dict)
        return JsonResponse(json_list, safe=True)  # 默认False,并做了json.dumps, 如果是字典的化,直接返回字典即可.


class ArticlesView3(View):
    '''
    使用django自带的序列化器
    '''

    def get(self, request):
        all_article = Articles.objects.all()
        from django.core import serializers  # 可以对任何字段进行序列化,但是对于imagefiled渲染时不会加Image_URL
        json_data = serializers.serialize('json', all_article)
        print(json_data)
        print(type(json_data))
        # return HttpResponse(json_data, content_type='application/json')
        import json
        json_list = json.loads(json_data)  # loads成原本类型,  dumps成一堆垃圾
        return JsonResponse(json_list, safe=False)
