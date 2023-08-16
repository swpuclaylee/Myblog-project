# --*--coding: utf-8 --*--
# @Time: 2023-08-14 21:04
# @Author: 李月初
# @FIle: task
from celery_tasks.celery import app
from django.core.mail import send_mail


@app.task
def send_mail_task(name, flag):
    if flag:
        subject = u"你有一条评论".encode('utf-8')
        message = u"你收到了一条来自{}的评论".format(name).encode('utf-8')
    else:
        subject = u'有人联系你了！'.encode('utf-8')
        message = u'你收到了一条来自{}的联系'.format(name).encode('utf-8')
    from_email = '1093591428@qq.com'
    recipients = ['swlz4751@gmail.com']
    send_mail(subject, message, from_email, recipients)
