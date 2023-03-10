# --*--coding: utf-8 --*--
# @Time: 2023-01-13 23:43
# @Author: 李月初
# @FIle: urls
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('article_category/<int:pk>/', views.article_category, name='article_category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('article/', views.article, name='article'),
    path('about/', views.abouts, name='about'),
]
