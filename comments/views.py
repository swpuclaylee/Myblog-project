from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CommentForm
from celery_tasks.task import send_mail_task
from django.core.mail import send_mail

import json
import logging
# Create your views here.

logger = logging.getLogger("comments")

@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request, messages.SUCCESS, '评论发表成功, 通过审核后展示！', extra_tags='success')
        name = json.dumps(comment.name)
        flag = 1
        try:
            send_mail_task.delay(name, flag)
        except Exception as e:
            logger.error('transfer send_mail_task failed in comments. reason: %s', e)
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