from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.CustomView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('signout/', views.CustomView.as_view(), name='signout'),
    path('idfinder/', views.idfinder, name='idfinder'),
    path('signin/kakao/', views.Kakao_login, name = "kakao_signin"),
    path('signin/kakao/callback', views.Kakao_login_callback, name="kakao_signin_callback"),
]