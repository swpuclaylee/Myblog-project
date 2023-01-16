from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category, Tag, Personal
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.conf import settings

import markdown
import re

# Create your views here.


# 全局变量
def global_settings(request):
    site_name = settings.SITE_NAME
    return locals()


# 分页
def paginator(request, post_list):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(post_list, 10, request=request)
    posts = p.page(page)
    return posts


# 首页
def index(request):
    post_list = Post.objects.all()
    posts = paginator(request, post_list)
    site_title = "首页"
    return render(request, 'blog/index.html', locals())


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    post.increase_views()
    site_title = "{}".format(post.title)
    return render(request, 'blog/detail.html', locals())


# 归档分类
def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    posts = paginator(request, post_list)
    site_title = "{}-{}".format(year, month)
    return render(request, 'blog/index.html', locals())


# 分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    posts = paginator(request, post_list)
    site_title = "{}".format(cate)
    return render(request, 'blog/index.html', locals())


# 标签分类
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    posts = paginator(request, post_list)
    site_title = '{}'.format(t)
    return render(request, 'blog/index.html', locals())


# 文章
def article(request):
    post_list = Post.objects.all()
    posts = paginator(request, post_list)
    site_title = "文章"
    return render(request, 'blog/article.html', locals())


# 关于
def abouts(request):
    personal_list = Personal.objects.all()
    for p in personal_list:
        p.per_info = markdown.markdown(p.per_info,
                                           extensions=[
                                               'markdown.extensions.extra',
                                               'markdown.extensions.codehilite',
                                               'markdown.extensions.toc',
                                           ])
    site_title = "关于"
    return render(request, 'blog/about.html', locals())


# 搜索
def search(request):
    q = request.GET.get('q')
    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    posts = paginator(request, post_list)
    return render(request, 'blog/search.html', locals())



