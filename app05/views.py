from django.http import HttpResponse
from django.shortcuts import render
from app05.forms import UserInfo
from django.views.generic.base import View


# Create your views here.

class UserinfoView(View):
    """
    用户个人信息
    """

    def get(self, request):
        user_info_obj = UserInfo(request.POST)  # 实例化form表单
        error_msg = user_info_obj.errors
        return render(request, "app05/index.html", {'user_info_obj': user_info_obj, 'errors': error_msg})  # 错误信息返回

    def post(self, request):
        user_info_form = UserInfo(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')
