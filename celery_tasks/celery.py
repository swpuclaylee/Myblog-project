# --*--coding: utf-8 --*--
# @Time: 2023-08-14 20:45
# @Author: 李月初
# @FIle: celery.py
from celery import Celery
from django.conf import settings

import os
import sys

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings.production')

app = Celery('celery_tasks')
app.config_from_object("celery_tasks.config")
app.autodiscover_tasks(['celery_tasks'])
