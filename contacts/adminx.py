# --*--coding: utf-8 --*--
# @Time: 2023-01-17 6:10
# @Author: 李月初
# @FIle: adminx
from .models import Contact, Links

import xadmin


class ContactAdmin:
    list_display = ['name', 'email', 'subject', 'created_time']
    fields = ['name', 'email', 'subject', 'message']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['-created_time']
    model_icon = 'fa fa-envelope'


class LinksAdmin:
    list_display = ['name', 'url', 'created_time']
    fields = ['name', 'url']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['-created_time']
    model_icon = 'fa fa-chain'


xadmin.site.register(Contact, ContactAdmin)
xadmin.site.register(Links, LinksAdmin)