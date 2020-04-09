from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('1', views.hello2, name='hello2'),
    path('2', views.hello3, name='hello3'),
    path('login', views.login, name='login'),  # 登录
    path('manage', views.manage, name='manage'),
    path('logout', views.logout, name='logout'),
]
