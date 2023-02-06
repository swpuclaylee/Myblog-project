# --*--coding: utf-8 --*--
# @Time: 2023-01-22 3:19
# @Author: 李月初
# @FIle: comments_cache
from django.core.cache import cache
from comments.models import Comment


def get_comments_cache(post):
    comment_list = cache.get('%s_comments_cached' % post.pk)
    if comment_list is None:
        comment_list = post.comment_set.filter(com_mod=Comment.YES).order_by('-created_time')
        cache.set('%s_comments_cached' % post.pk, comment_list)
    return comment_list

