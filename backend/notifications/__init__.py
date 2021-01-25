from django.apps import AppConfig


class NotificationsAppConfig(AppConfig):
    name = 'notifications'
    label = 'notifications'
    verbose_name = 'Notifications'

    def ready(self):
        import notifications.signals

default_app_config = 'notifications.NotificationsAppConfig'
