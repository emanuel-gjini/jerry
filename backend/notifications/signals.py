from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from articles.models import Comment
from profiles.models import Profile, follow_updated
from .models import Notification


@receiver(post_save, sender=Comment)
def create_notifications_for_new_comments(sender, instance, created, *args, **kwargs):
    if instance and created:
        Notification.objects.create(
            user = instance.article.author.user,
            message = 'User "{}" commented in your article "{}"'.format(
                instance.article.author.user,
                instance.article
            )
        )

@receiver(follow_updated, sender=Profile)
def create_notifications_for_follows(sender, instance, follow, profile, *args, **kwargs):
    if instance:
        if follow:
            message = 'User "{}" started following you'.format(profile.user)
        else:
            message = 'User "{}" unfollowed you'.format(profile.user)
        Notification.objects.create(
            user = profile.user,
            message = message
        )

@receiver(post_save, sender=Notification)
def dispatch_notifications_to_users(sender, instance, created, *args, **kwargs):
    if instance and created:
        # Dispatch to websockets
        instance.user.send_notification(instance.__str__())
