from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.


class Comment(models.Model):
    YES = 'Y'
    NO = 'N'

    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = RichTextField('内容', config_name='comment')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    COM_MOD_CHOICES = [
        (YES, 'yes'),
        (NO, 'no'),
    ]
    com_mod = models.CharField(
        max_length=10,
        choices=COM_MOD_CHOICES,
        default=NO,
        verbose_name='评论审核',
    )

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
