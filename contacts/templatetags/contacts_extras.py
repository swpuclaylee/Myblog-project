# --*--coding: utf-8 --*--
# @Time: 2023-01-14 1:55
# @Author: 李月初
# @FIle: comments_extras

from django import template
from ..models import Links


register = template.Library()


@register.inclusion_tag('contacts/inclusions/_links.html', takes_context=True)
def show_links(context):
    url_list = Links.objects.all()
    return {
        'url_list': url_list,
    }
