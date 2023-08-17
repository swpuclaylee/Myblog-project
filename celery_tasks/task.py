# --*--coding: utf-8 --*--
# @Time: 2023-08-14 21:04
# @Author: 李月初
# @FIle: task
from celery_tasks.celery import app
from django.core.mail import send_mail

import pickle


@app.task
def send_mail_task(name, flag):
    name = pickle.loads(name)
    #d_name = name.encode('utf-8').decode('unicode_escape')
    if flag:
        subject = "you have a comment"
        message = f"you received a comment from{name}"
    else:
        subject = 'someone to contact'
        message = f'you received a contact from{name}'
    from_email = '1093591428@qq.com'
    recipients = ['swlz4751@gmail.com']
    send_mail(subject, message, from_email, recipients)
