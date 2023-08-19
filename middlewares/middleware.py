# --*--coding: utf-8 --*--
# @Time: 2023-08-19 21:39
# @Author: 李月初
# @FIle: middleware
from blogproject.settings.common import GLOBAL_VIEW_COUNT
from django.core.cache import cache


class GlobalViewCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.path.startswith('/xadmin/') and response.status_code == 200 and request.method == "GET":  # 排除管理员后台的请求
            # 递增全局浏览量
            GLOBAL_VIEW_COUNT = cache.get('global_view_count', 1)
            cache.set('global_view_count', GLOBAL_VIEW_COUNT + 1)
        return response
