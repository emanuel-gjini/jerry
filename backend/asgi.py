"""
ASGI config for jerry project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from authentication.backends import ChannelJWTAuthentication
from notifications.consumers import NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')



application = ProtocolTypeRouter({
    'websocket': ChannelJWTAuthentication(
        URLRouter(
        [
            url('', NotificationConsumer.as_asgi())
        ]
    )
  )
})