# --*--coding: utf-8 --*--
# @Time: 2023-01-14 3:50
# @Author: 李月初
# @FIle: production
from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '139.224.56.80']

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://139.224.56.80:9200/'