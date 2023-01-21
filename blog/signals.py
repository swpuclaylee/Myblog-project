# --*--coding: utf-8 --*--
# @Time: 2023-01-21 14:36
# @Author: 李月初
# @FIle: signals
from django.db.models.signals import post_delete, post_save
from .models import Post
from django.dispatch import receiver
from django.core.cache import cache
from django.utils import timezone


# 文章缓存更新
@receiver(post_save, sender=Post)
def cache_post_save_handler(sender, instance, *args, **kwargs):
    year = timezone.now().year
    month = timezone.now().month
    cache.delete('cached_posts')
    cache.delete('archive_cached_posts:%syear%smonth' % (year, month))
    cache.delete('category_cached_posts:%s' % instance.category.pk)
    # 标签：保留，instance.tags拿不到tags对象
    #cache.delete('tag_cached_posts:%s' % instance.tags.pk)


# 文章缓存更新
@receiver(post_delete, sender=Post)
def cache_post_delete_handler(sender, instance, *args, **kwargs):
    year = timezone.now().year
    month = timezone.now().month
    cache.delete('cached_posts')
    cache.delete('archive_cached_posts:%syear%smonth' % (year, month))
    cache.delete('category_cached_posts:%s' % instance.category.pk)
    # 标签：保留，instance.tags拿不到tags对象
    #cache.delete('tag_cached_posts:%s' % instance.tags.pk)
