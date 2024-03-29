# --*--coding: utf-8 --*--
# @Time: 2023-08-14 21:04
# @Author: 李月初
# @FIle: task
from celery_tasks.celery import app
from django.core.mail import send_mail
from celery.utils.log import get_task_logger

import json


logger = get_task_logger('celerylog')


@app.task
def send_mail_task(name, flag):
    name = json.loads(name)
    logger.info(f"the name is {name}")
    if flag:
        subject = "you have a comment"
        message = f"you received a comment from{name}"
    else:
        subject = 'someone to contact'
        message = f'you received a contact from{name}'
    from_email = '1093591428@qq.com'
    recipients = ['yunchu5587@gmail.com']
    try:
        logger.info(message)
        send_mail(subject, message, from_email, recipients)
    except Exception as e:
        logger.error("transfer send_mail failed in celery task. reason: %s", e)
