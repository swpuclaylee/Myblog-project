# --*--coding: utf-8 --*--
# @Time: 2023-01-14 1:40
# @Author: 李月初
# @FIle: blog_extras
from django import template
from django.db.models.aggregates import Count
from django.db.models.functions import ExtractMonth, ExtractYear
from ..models import Post, Category, Tag
from ..get_save_cache import get_cached_posts

register = template.Library()


@register.inclusion_tag('blog/inclusions/_read_rank.html', takes_context=True)
def read_rank_posts(context, num=6):
    return {
        'read_rank_post_list': get_cached_posts().order_by('-views')[:num],
    }


@register.inclusion_tag('blog/inclusions/_comment_rank.html', takes_context=True)
def comment_rank_posts(context, num=6):
    posts = get_cached_posts()
    non_zero_comment_posts = [post for post in posts if post.comment_set.count() > 0]
    return {
        'comment_rank_post_list': non_zero_comment_posts.annotate(comment_count=Count('comment')).order_by('-comment_count')[:num],
    }

@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': get_cached_posts().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.annotate(year=ExtractYear('created_time'), month=ExtractMonth('created_time')) \
.values('year', 'month').order_by('-year', '-month').annotate(num_posts=Count('id')),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'tag_list': tag_list,
    }