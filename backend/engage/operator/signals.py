# coding: utf-8

from django.dispatch import receiver
from django.db.models.signals import post_save

from engage.core.models import Notifications as NotificationsModel
from engage.services import Notifications
from engage.core.constants import NotificationTemplate
from .constants import AdType
from .models import Operator, OperatorAd


@receiver(post_save, sender=Operator)
def new_operator(sender, instance, created, **kwargs):
    if not created:
        return


@receiver(post_save, sender=OperatorAd)
def new_operator_ads(sender, instance, created, **kwargs):
    if created and instance.ad_type == AdType.VIDEO:
        notifications = NotificationsModel.objects.filter(
            template=NotificationTemplate.VIDEO_ADDED,
            is_active=True
        ).all()

        for notification in notifications:
            Notifications.bulk(notification)

