from django.apps import AppConfig


class CommentsConfig(AppConfig):
    name = 'comments'
    verbose_name = '评论'

    def ready(self):
        import comments.signals
