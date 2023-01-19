from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.utils.functional import cached_property
from ckeditor_uploader.fields import RichTextUploadingField

import markdown
import re
# Create your models here.


# markdown解析
def generate_rich_content(value):
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    toc = m.group(1) if m is not None else ""
    return {"content": content, "toc": toc}


# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    body = RichTextUploadingField('正文')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body.replace('&nbsp;', ''))).lstrip()[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    @property
    def toc(self):
        return self.rich_content.get("toc", "")

    @property
    def body_html(self):
        return self.rich_content.get("content", "")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)


class Personal(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='图片路径', blank=False, null=False, default='')
    per_info = RichTextUploadingField('简介')
    github = models.URLField('github', max_length=120, default='')

    def __str__(self):
        return self.per_info[:10]

    class Meta:
        verbose_name = '个人信息'
        verbose_name_plural = verbose_name

    @property
    def body_html(self):
        return self.rich_content.get("content", "")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.per_info)

    @property
    def personal_information(self):
        return strip_tags(self.per_info)

