from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    seen = serializers.BooleanField()
    message = serializers.CharField()
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Notification
        fields = ('id', 'message', 'seen', 'updatedAt', 'createdAt')
        read_only_fields = ('id', 'message',)

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()