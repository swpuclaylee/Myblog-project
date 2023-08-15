# --*--coding: utf-8 --*--
# @Time: 2023-08-14 20:45
# @Author: 李月初
# @FIle: celery.py
from celery import Celery
from django.conf import settings

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Myblog-project.blogproject.settings.production')

app = Celery('celery_tasks')
app.config_from_object("celery_tasks.config")
app.autodiscover_tasks(['celery_tasks'])
