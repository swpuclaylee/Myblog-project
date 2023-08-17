from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CommentForm
from celery_tasks.task import send_mail_task
from django.core.mail import send_mail

import codecs
# Create your views here.


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request, messages.SUCCESS, '评论发表成功, 通过审核后展示！', extra_tags='success')
        try:
            name = comment.name.encode('utf-8')
            #name = codecs.encode(comment.name, 'ascii').decode('ascii')
            send_mail_task.delay(name, 1)
        except Exception as e:
            subject = '评论报错'
            message = f'错误原因：{e}'
            from_email = '1093591428@qq.com'
            recipients = ['swlz4751@gmail.com']
            send_mail(subject, message, from_email, recipients)
        #send_mail_task.delay(comment.name, 1)
        return redirect(post)
    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)


# *************************************************
#             rest api
# *************************************************
from rest_framework import mixins, viewsets
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()