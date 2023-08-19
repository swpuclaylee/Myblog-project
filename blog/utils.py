# --*--coding: utf-8 --*--
# @Time: 2023-01-20 5:31
# @Author: 李月初
# @FIle: utils
from django.utils.html import strip_tags
from haystack.utils import Highlighter as HaystackHighlighter
from django.conf import settings
from pure_pagination import Paginator, PageNotAnInteger
from blog.get_save_cache import get_cached_site_view


# 搜索高亮
class Highlighter(HaystackHighlighter):
    def highlight(self, text_block):
        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        start_offset, end_offset = self.find_window(highlight_locations)
        if len(text_block) < self.max_length:
            start_offset = 0
        return self.render_html(highlight_locations, start_offset, end_offset)


# 全局变量
def global_settings(request):
    global_view_count = get_cached_site_view()
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




