# --*--coding: utf-8 --*--
# @Time: 2023-01-22 3:30
# @Author: 李月初
# @FIle: signals
from django.db.models.signals import post_delete, post_save
from .models import Comment
from django.dispatch import receiver
from django.core.cache import cache


# 评论缓存更新
@receiver(post_save, sender=Comment)
def cache_comment_save_handler(sender, instance, *args, **kwargs):
    cache.delete('%s_comments_cached' % instance.post.pk)


@receiver(post_delete, sender=Comment)
def cache_comment_delete_handler(sender, instance, *args, **kwargs):
    cache.delete('%s_comments_cached' % instance.post.pk)
