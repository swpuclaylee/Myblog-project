# --*--coding: utf-8 --*--
# @Time: 2023-01-15 3:23
# @Author: 李月初
# @FIle: urls


from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('contact/', views.contact, name='contact')
]