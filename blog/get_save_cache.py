# --*--coding: utf-8 --*--
# @Time: 2023-01-21 11:54
# @Author: 李月初
# @FIle: get_save_cache
from django.core.cache import cache
from .models import Post, Category
from django.shortcuts import get_object_or_404


# 所有文章
def get_cached_posts():
    post_list = cache.get('cached_posts')
    if post_list is None:
        post_list = Post.objects.all()
        cache.set('cached_posts', post_list)
    return post_list


# 归档文章
def get_archive_cached_posts(year, month):
    post_list = cache.get('archive_cached_posts:%syear%smonth' % (year, month))
    if post_list is None:
        post_list = Post.objects.filter(
            created_time__year=year,
            created_time__month=month).order_by('-created_time')
        cache.set('archive_cached_posts:%syear%smonth' % (year, month), post_list)
    return post_list


# 分类文章
def get_category_cached_posts(pk):
    post_list = cache.get('category_cached_posts:%s' % pk)
    cate = get_object_or_404(Category, pk=pk)
    if post_list is None:
        post_list = Post.objects.filter(category=cate).order_by('-created_time')
        cache.set('category_cached_posts:%s' % pk, post_list)
    return post_list, cate


# 标签分类：保留，有问题。
# def get_tag_cached_posts(pk):
#     post_list = cache.get('tag_cached_posts:%s' % pk)
#     print(post_list)
#     t = get_object_or_404(Tag, pk=pk)
#     if post_list is None:
#         print("缓存为空")
#         post_list = Post.objects.filter(tags=t).order_by('-created_time')
#         cache.set('tag_cached_posts:%s' % pk, post_list)
#     return post_list, t


