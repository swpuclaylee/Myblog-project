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
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
    path('article/', views.ArticleView.as_view(), name='article'),
    path('about/', views.abouts, name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)