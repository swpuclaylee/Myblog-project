# --*--coding: utf-8 --*--
# @Time: 2023-08-19 21:39
# @Author: 李月初
# @FIle: middleware
from django.core.cache import cache
from blog.models import SiteView



class GlobalViewCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.path.startswith('/xadmin/') and response.status_code == 200 and request.method == "GET":  # 排除管理员后台的请求
            site_view_obj = SiteView.objects.first()
            if site_view_obj:
                GLOBAL_VIEW_COUNT = site_view_obj.site_view_count
            else:
                GLOBAL_VIEW_COUNT = int(cache.get('global_view_count', 0))
            cache.set('global_view_count', GLOBAL_VIEW_COUNT + 1)
            if not site_view_obj:
                SiteView.objects.create(site_view_count=GLOBAL_VIEW_COUNT)
            else:
                site_view_obj.site_view_count = GLOBAL_VIEW_COUNT
                site_view_obj.save()

            # # 递增全局浏览量
            # GLOBAL_VIEW_COUNT = cache.get('global_view_count', 0)
            # cache.set('global_view_count', GLOBAL_VIEW_COUNT + 1)
            # site_view = SiteView.objects.first()  # 假设 SiteView 模型只有一个对象
            # if not site_view:
            #     SiteView.objects.create(site_view_count=GLOBAL_VIEW_COUNT)
            # else:
            #     site_view.site_view_count = GLOBAL_VIEW_COUNT
            #     site_view.save()
        return response
