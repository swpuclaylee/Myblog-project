# --*--coding: utf-8 --*--
# @Time: 2023-01-14 3:50
# @Author: 李月初
# @FIle: local
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://127.0.0.1:9200/'