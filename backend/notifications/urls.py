from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import NotificationsAPIViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'notifications', NotificationsAPIViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]