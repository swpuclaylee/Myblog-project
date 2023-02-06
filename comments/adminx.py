# --*--coding: utf-8 --*--
# @Time: 2023-01-17 6:03
# @Author: 李月初
# @FIle: adminx
from .models import Comment

import xadmin


class CommentAdmin:
    list_display = ['name', 'email', 'url', 'post', 'created_time', 'com_mod']
    fields = ['name', 'email', 'url', 'text', 'post', 'com_mod']
    search_fields = ['name', 'post__title']
    list_filter = ['name', 'post__title']
    list_per_page = 10
    ordering = ['-created_time']
    model_icon = 'fa fa-comments'


xadmin.site.register(Comment, CommentAdmin)
