# --*--coding: utf-8 --*--
# @Time: 2023-01-17 4:34
# @Author: 李月初
# @FIle: adminx
from .models import Category, Tag, Personal, Post, SiteView
from xadmin import views
from django.utils.html import strip_tags

import xadmin


# 后台主题
class AdminSettings:
    enable_themes = True
    use_bootswatch = True


# 标题
class GlobalSettings(object):
    site_title = 'clay的博客 '
    site_footer = 'claylwz.com'
    # 菜单样式设置
    menu_style = 'accordion'


class CategoryAdmin:
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['-id']
    model_icon = 'fa fa-bell'


class TagAdmin:
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['-id']
    model_icon = 'fa fa-tag'


class SiteViewAdmin:
    list_display = ['site_view_count']
    search_fields = ['site_view_count']
    list_filter = ['site_view_count']
    readonly_fields = ['site_view_count']
    model_icon = 'fa fa-anchor'

    def has_add_permission(self):
        return False

    def has_delete_permission(self, request=None, obj=None):
        return False

    def has_change_permission(self, obj=None):
        return False


class PostAdmin:
    list_display = ['title', 'created_time', 'modified_time', 'category', 'views', 'comments_count']
    fields = ['title', 'body', 'category', 'tags']
    search_fields = ['title']
    list_filter = ['title', 'category']
    list_per_page = 10
    ordering = ['-created_time']
    model_icon = 'fa fa-bookmark'

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        obj.save()

    def comments_count(self, obj):
        return obj.comment_set.all().count()
    comments_count.short_description = '评论数量'


class PersonalAdmin(xadmin.views.ModelAdminView):
    list_display = ['image', 'introduction', 'github']
    search_fields = ['per_info']
    list_filter = ['per_info']
    list_per_page = 5
    model_icon = 'fa fa-user-circle'

    def has_add_permission(self):
        return False if self.model.objects.count() > 0 else super().has_add_permission()

    def has_delete_permission(self, request=None, obj=None):
        return True

    def introduction(self, obj):
        return strip_tags(obj.per_info.replace('&nbsp;', '').replace('&ldquo;', '').replace('&rdquo;', '')[:20])
    introduction.short_description = '简介'


xadmin.site.register(Personal, PersonalAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(views.BaseAdminView, AdminSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(SiteView, SiteViewAdmin)
