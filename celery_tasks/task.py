# --*--coding: utf-8 --*--
# @Time: 2023-08-14 21:04
# @Author: 李月初
# @FIle: task
from celery_tasks.celery import app
from django.core.mail import send_mail


@app.task
def send_mail_task(name, flag):
    if flag:
        subject = "you have a comment".encode('utf-8')
        message = "you received a comment from{}".format(name).encode('utf-8')
    else:
        subject = 'someone to contact'.encode('utf-8')
        message = 'you received a contact from{}'.format(name).encode('utf-8')
    from_email = '1093591428@qq.com'
    recipients = ['swlz4751@gmail.com']
    send_mail(subject, message, from_email, recipients)
