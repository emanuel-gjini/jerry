from core.renderers import JerryJSONRenderer


class NotificationJSONRenderer(JerryJSONRenderer):
    object_label = 'notification'
    pagination_object_label = 'notifications'
    pagination_count_label = 'notificationsCount'
