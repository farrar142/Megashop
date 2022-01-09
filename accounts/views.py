import os
from django.http.response import HttpResponseNotAllowed

import requests
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import (
    logout_then_login, LoginView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from .forms import SignupForm
from .models import User
from .protected import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import classonlymethod
import logging
logger = logging.getLogger('django.request')
from django.contrib.auth import views as auth_views

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            # signed_user.send_welcome_email()  # FIXME: Celery로 처리하는 것을 추천.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def idfinder(request):
    if request.method == 'POST':
        # messages.success(request, request.POST.get('email'))
        email = request.POST.get('email')
        if email == '':
            messages.warning(request,'Email을 입력 해 주세요')
            return render(request, 'accounts/idfinder.html')
        try:
            user = User.objects.get(email=email)
            messages.success(request,f"ID : {user.username}")
        except:
            messages.error(request,'회원 정보가 없어요')
            return render(request, 'accounts/idfinder.html')
        return redirect('accounts:signin')
    return render(request, 'accounts/idfinder.html')

def Kakao_login(request : HttpRequest):
    REST_API_KEY = KAKAO_APP__REST_API_KEY
    REDIRECT_URI = KAKAO_APP__LOGIN__REDIRECT_URI
    kakao_auth_api = "https://kauth.kakao.com/oauth/authorize?"
    return redirect(
        f"{kakao_auth_api}client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    )
def Kakao_login_callback(request):
    code = request.GET.get("code")
    REST_API_KEY = KAKAO_APP__REST_API_KEY
    REDIRECT_URI = KAKAO_APP__LOGIN__REDIRECT_URI
    
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}"
    )

    token_json = token_request.json()

    error = token_json.get("error", None)
    if error is not None:
        raise Exception('카카오 로그인 에러')

    access_token = token_json.get("access_token")

    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()

    id = profile_json.get("id")

    User.login_with_kakao(request, id)
    user = User.objects.get(provider_accounts_id=id)
    messages.success(request, f"{user.username}님 카카오톡 계정으로 로그인되었습니다")

    return redirect("index")



class CustomView(LoginView):
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.data.get('refresh'):
            self.refresh_page()
        return super().post(self, request, *args, **kwargs)

    @csrf_exempt
    def refresh_page(self):

        return redirect("index")
    
    @classonlymethod
    def as_view(cls, **initkwargs):
        super().as_view()