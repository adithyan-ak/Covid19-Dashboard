from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]