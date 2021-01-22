from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'jerry.apps.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import jerry.apps.articles.signals

default_app_config = 'jerry.apps.articles.ArticlesAppConfig'
