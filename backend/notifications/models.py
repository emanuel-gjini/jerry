import json
from django.db import models
from core.models import TimestampedModel


class Notification(TimestampedModel):
    # A notification is tied to a specific user
    user = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='notifications'
    )
    # Each notification has a message to show to the user
    message = models.TextField(blank=True)
    # Is the notification seen or not
    seen = models.BooleanField(default=False)

    def __str__(self):
        return json.dumps({
            'id': self.pk,
            'user': self.user.email,
            'message': self.message,
            'seen': self.seen,
            'createdAt': self.created_at.isoformat(),
        })