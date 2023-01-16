# --*--coding: utf-8 --*--
# @Time: 2023-01-17 6:10
# @Author: 李月初
# @FIle: adminx
from .models import Contact

import xadmin


class ContactAdmin:
    list_display = ['name', 'email', 'topic', 'created_time']
    fields = ['name', 'email', 'topic', 'text']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
    ordering = ['-created_time']
    model_icon = 'fa fa-envelope'


xadmin.site.register(Contact, ContactAdmin)