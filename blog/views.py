from django.shortcuts import get_object_or_404, render
from .utils import paginator
from .get_save_cache import get_cached_posts, get_archive_cached_posts, get_category_cached_posts
from .models import Post, Personal, Tag


# 首页
def index(request):
    post_list = get_cached_posts()
    posts = paginator(request, post_list)
    site_title = "首页"
    return render(request, 'blog/index.html', locals())


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    site_title = "{}".format(post.title)
    return render(request, 'blog/detail.html', locals())


# 归档分类
def archive(request, year, month):
    if year < 2000 or year >= 3000 or month < 1 or month > 12:
        return page_not_found(request)
    post_list = get_archive_cached_posts(year, month)
    posts = paginator(request, post_list)
    site_title = "{}-{}".format(year, month)
    return render(request, 'blog/index.html', locals())


# 分类
def category(request, pk):
    post_list, cate = get_category_cached_posts(pk)
    posts = paginator(request, post_list)
    site_title = "{}".format(cate)
    return render(request, 'blog/index.html', locals())


# 标签分类，暂时用cache_page
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    posts = paginator(request, post_list)
    site_title = '{}'.format(t)
    return render(request, 'blog/index.html', locals())


# 文章
def article(request):
    post_list = get_cached_posts()
    posts = paginator(request, post_list)
    site_title = "文章"
    return render(request, 'blog/article.html', locals())


# 关于
def abouts(request):
    personal_list = Personal.objects.all()
    site_title = "关于"
    return render(request, 'blog/about.html', locals())


# 404
def page_not_found(request, exception=None):
    return render(request, 'blog/404.html', status=404)


# 500
def page_error(request):
    return render(request, 'blog/500.html', status=500)

