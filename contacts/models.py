from django.db import models
from django.utils import timezone
# Create your models here.


class Contact(models.Model):
    name = models.CharField('名字', max_length=128)
    email = models.EmailField('邮箱')
    topic = models.CharField('主题', max_length=50)
    text = models.TextField('内容')
    created_time = models.DateTimeField('评论时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '联系'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def save(self, *args, **kwargs):
        self.created_time = timezone.now()
        super().save(*args, **kwargs)
