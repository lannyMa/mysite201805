from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print(request.META)
    print(request.method)
    print(request.body)
    return HttpResponse(request.get_signed_cookie())


def home(request):
    data = {
        'name': 'maotai',
        'age': 22
    }
    import json
    return HttpResponse(json.dumps(data), content_type='application/json', status=400)


def home2(request):
    data = {'name': 'maotai', 'age': 23}
    data2=[1,2,3]
    return JsonResponse(data2,safe=False) #safe默认true, 仅在list时置为false
