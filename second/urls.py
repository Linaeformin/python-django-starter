from django.urls import path, re_path
from . import views

urlpatterns = [
    path('list/', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('confirm/', views.confirm, name="confirm")
]
