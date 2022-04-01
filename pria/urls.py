from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mypage', views.mypage, name='mypage'),
]
