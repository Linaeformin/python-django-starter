from django.urls import path, re_path
from . import views
urlpatterns=[
    path('', views.index,name='index'), #도메인을 치자마자 보여지는 창은 index, index를 path에 연결
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),
]