"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from blog.feeds import PostRssFeed
from django.conf.urls.static import static, serve
from .settings.common import MEDIA_URL, MEDIA_ROOT, STATIC_ROOT
from blog.views import page_not_found, page_error
from rest_framework import routers
from blog import views
from comments.views import CommentViewSet

import xadmin

router = routers.DefaultRouter()

# 视图集
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register('tags', views.TagViewSet, basename='tag')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r"search", views.PostSearchView, basename="search")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include('blog.urls')),
    path('', include('comments.urls')),
    path('', include('contacts.urls')),
    path('all/rss', PostRssFeed(), name='rss'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    path('search/', include('haystack.urls')),

    # djangorestframework
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("api/v1/", include((router.urls, "api"), namespace="v1")),

    # rest api
    # 普通视图函数
    #path('api/index/', views.rindex)

    #通用视图函数
    #path('api/index/', views.IndexPostListView.as_view())

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = page_not_found
handler500 = page_error
