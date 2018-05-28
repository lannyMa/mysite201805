from django.http import HttpResponse
from django.shortcuts import render
from app05.forms import UserInfo


# Create your views here.

def index(request):
    user_info_obj = UserInfo(request.POST)  # 实例化form表单
    if request.method == "GET":
        error_msg = user_info_obj.errors
        return render(request, "app05/index.html", {'user_info_obj': user_info_obj, 'errors': error_msg})  # 错误信息返回
    elif request.method == "POST":
        request.POST.get("email")
