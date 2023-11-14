from django.apps import AppConfig
from django.core.cache import cache
from .models import SiteView


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客'

    def ready(self):
        import blog.signals

        site_view_obj = SiteView.objects.first()
        if site_view_obj:
            cache.set('global_view_count', site_view_obj.site_view_count)

