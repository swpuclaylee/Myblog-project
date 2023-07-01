from django.shortcuts import get_object_or_404, render
from .utils import paginator
from .get_save_cache import get_cached_posts, get_archive_cached_posts, get_category_cached_posts
from .models import Post, Personal, Tag, Category


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


# 分类
def article_category(request, pk):
    print(111)
    post_list, cate = get_category_cached_posts(pk)
    posts = paginator(request, post_list)
    site_title = "{}".format(cate)
    return render(request, 'blog/article.html', locals())


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
# def page_not_found(request, exception=None):
#     return render(request, 'blog/404.html', status=404)
#
#
# # 500
# def page_error(request):
#     return render(request, 'blog/500.html', status=500)



# ********** restframework api ************
from .serializers import PostListSerializer, PostRetrieveSerializer, CategorySerializer, TagSerializer


# 普通视图函数
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# @api_view(http_method_names=['GET'])
# def rindex(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     serializer = PostListSerializer(post_list, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# 通用类试图
# from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import AllowAny
#
#
# class IndexPostListView(ListAPIView):
#     serializer_class = PostListSerializer
#     queryset = Post.objects.all()
#     pagination_class = PageNumberPagination
#     permission_classes = [AllowAny]

# 视图集
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.serializers import DateField
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from comments.serializers import CommentSerializer


# 首文章列表或详情页接口
class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

    serializer_class_table = {
        'list': PostListSerializer,
        'retrieve': PostRetrieveSerializer,
    }

    # 过滤，获取分类、归档、标签下的文章
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def get_serializer_class(self):
        return self.serializer_class_table.get(self.action, super().get_serializer_class)

    # 归档列表
    @action(methods=["GET"], detail=False, url_path="archive/dates", url_name="archive-date")
    def list_archive_dates(self, request, *args, **kwargs):
        dates = Post.objects.dates("created_time", "month", order="DESC")
        date_filed = DateField()
        data = [date_filed.to_representation(date) for date in dates]
        return Response(data=data, status=status.HTTP_200_OK)

    # 获取文章下评论
    @action(
            methods=["GET"],
            detail=True,
            url_path="comments",
            url_name="comment",
            pagination_class=LimitOffsetPagination,
            serializer_class=CommentSerializer,
    )
    def list_comments(self, request, *args, **kwargs):
        # 根据 URL 传入的参数值（文章 id）获取到博客文章记录
        post = self.get_object()
        # 获取文章下关联的全部评论
        queryset = post.comment_set.all().order_by("-created_time")
        # 对评论列表进行分页，根据 URL 传入的参数获取指定页的评论
        page = self.paginate_queryset(queryset)
        # 序列化评论
        serializer = CommentSerializer(page, many=True)
        # 返回分页后的评论列表
        return self.get_paginated_response(serializer.data)


# 文章分类接口
class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None
    permission_classes = [AllowAny]


# 标签分类接口
class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    pagination_class = None


# 搜索
from drf_haystack.viewsets import HaystackViewSet
from .serializers import PostHaystackSerializer

# 自定义限流时间
from rest_framework.throttling import AnonRateThrottle


class PostSearchAnonRateThrottle(AnonRateThrottle):
    THROTTLE_RATES = {"anon": "5/min"}


class PostSearchView(HaystackViewSet):
    index_models = [Post]
    serializer_class = PostHaystackSerializer
    throttle_classes = [PostSearchAnonRateThrottle]


