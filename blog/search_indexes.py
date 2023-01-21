# --*--coding: utf-8 --*--
# @Time: 2023-01-20 5:18
# @Author: 李月初
# @FIle: search_indexes

from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()