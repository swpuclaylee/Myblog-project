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
from django.views.generic.base import RedirectView

import xadmin


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
    path('^favicon\.ico$', RedirectView.as_view(url=r'media/images/logo.png')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = page_not_found
handler500 = page_error
