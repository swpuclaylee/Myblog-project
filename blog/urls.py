# --*--coding: utf-8 --*--
# @Time: 2023-01-13 23:43
# @Author: 李月初
# @FIle: urls
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('search/', views.search, name='search'),
    path('article/', views.article, name='article'),
    path('about/', views.abouts, name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)