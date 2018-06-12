from django.http import HttpResponse
from django.shortcuts import render
from app08.forms import UserAskForm
from django.views.generic import View


# Create your views here.

def index(request):
    return render(request, "app08/org_list.html")


class AddUserAskView(View):
    """
    用户添加咨询
    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')
