# --*--coding: utf-8 --*--
# @Time: 2023-01-14 6:14
# @Author: 李月初
# @FIle: fake

import os
import sys
import django


# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogproject.settings.local")
    django.setup()

    from blog.models import Category, Post, Tag
    from comments.models import Comment

    print('clean database')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Comment.objects.all().delete()

    print('done!')