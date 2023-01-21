# --*--coding: utf-8 --*--
# @Time: 2023-01-14 1:55
# @Author: 李月初
# @FIle: comments_extras

from django import template
from ..forms import CommentForm
from ..comments_cache import get_comments_cache

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }


@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = get_comments_cache(post)
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }