# --*--coding: utf-8 --*--
# @Time: 2023-01-17 0:23
# @Author: 李月初
# @FIle: feeds
from django.contrib.syndication.views import  Feed
from .models import Post


class PostRssFeed(Feed):
    title = "clay的博客"
    link = '/'
    description = "clay的博客 全部文章"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return "[%s], %s" % (item.category, item.title)

    def item_description(self, item):
        return item.body_html
