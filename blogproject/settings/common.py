"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps')) # 把extra_apps文件夹添加到搜索目录中

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'comments.apps.CommentsConfig',
    'pure_pagination',
    'contacts.apps.ContactsConfig',
    'xadmin',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.global_settings',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)


# django-pure-pagination 分页设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 4, # 分页条当前页前后应该显示的总页数（两边均匀分布，因此要设置为偶数），
    'MARGIN_PAGES_DISPLAYED': 2, # 分页条开头和结尾显示的页数
    'SHOW_FIRST_PAGE_WHEN_INVALID': True, # 当请求了不存在页，显示第一页
}

# 配置 MEDIA_ROOT 作为你上传文件在服务器中的基本路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
# 配置 MEDIA_URL 作为公用 URL，指向上传文件的基本路径
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'cke_uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

# 网站基本信息
SITE_NAME = 'clay的博客'


# 富文本编辑器配置
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width':'auto',
        'height':'250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 格式、字体、大小
            ['Format', 'Font', 'FontSize'],
            #居左，居中，居右
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Image', 'Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet', 'image2', 'widget', 'lineutils',]),
    }
}