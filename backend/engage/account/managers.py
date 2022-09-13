# coding: utf-8

from re import template
from django.db import models, transaction
from django.db.models import Count, Sum, Case, When, F, Value
from django.db.models.functions import Coalesce
from django.utils.timezone import now
from django.contrib.auth.models import UserManager



from engage.core.constants import NotificationTemplate
from .constants import FriendStatus, CoinTransaction

__all__ = (
    'CustomUserManager',
    'UserActivityManager'
)

class CustomUserManager(UserManager):

    def is_friend(self, friend):
        return self.get_queryset().filter(
            friendlist__friend=friend,
            status=FriendStatus.ACCEPTED
        )

    def with_stats(self):
        return self.get_queryset().annotate(
            total_matches=Count(''),
            won_matches=Count(''),
            lost_matches=Count('')
        ).filter()

    def with_balance(self):
        return self.get_queryset().annotate(
            balance=Coalesce(Sum(
                Case(
                    When(usertransactionhistory__action=CoinTransaction.REDEEM,
                         then=F('usertransactionhistory__amount') * -1),
                    default=F('usertransactionhistory__amount')
                )
            ), Value(0))
        )


class UserActivityManager(models.Manager):
    @staticmethod
    def since_join_days(user):
        return (now().date() - user.created.date()).days

    def was_active_between(self, user, dates):
        return self.filter(user=user, day__in=dates).exists()

    def was_all_active_between(self, user, dates):
        return self.filter(user=user, day__in=dates).count() == len(dates)

    def get_active_count(self,user):
        return self.filter(user=user,was_active=True).count()
    @transaction.atomic()
    def set_active_day(self, current_user):
        from .models import UserLevelHistory
        from .models import UserNotification
        from engage.services import notify_when
        
        day = now().date()
        activity, created = self.get_or_create(
            user=current_user,
            day=day,
            defaults={'was_active': True}
        )
        if created:
            if  current_user.is_billed == False:
                UserLevelHistory.objects.create(
                    user=current_user,
                    level=1
                )

            @notify_when(events=[NotificationTemplate.DAILY], is_route=False, is_one_time=False)
            def notify(user, user_notifications):
                """ extra logic if needed """
            notify(user=current_user)

            active_count = self.get_active_count(current_user)
            if active_count == 5:
                get_notification = UserNotification.objects.filter(
                    user=current_user,
                    notification__template=NotificationTemplate.ACTIVE_5_DAYS).first()
                print(get_notification)    
                if not get_notification : 
                    @notify_when(events=[NotificationTemplate.ACTIVE_5_DAYS], is_route=False)
                    def notify(user, user_notifications):
                        """ extra logic if needed """
                    notify(user=current_user)
                
            elif active_count == 10:
                get_notification = UserNotification.objects.filter(
                    user=current_user,
                    notification__template=NotificationTemplate.ACTIVE_10_DAYS).first()
                if not get_notification :     
                    @notify_when(events=[NotificationTemplate.ACTIVE_10_DAYS], is_route=False)
                    def notify(user, user_notifications):
                        """ extra logic if needed """
                    notify(user=current_user)
                    @notify_when(events=[NotificationTemplate.LEVEL_UP_10], is_route=False)
                    def notify(user, user_notifications):
                        """ extra logic if needed """
                    notify(user=current_user)

            elif active_count == 30:
                get_notification = UserNotification.objects.filter(
                    user=current_user,
                    notification__template=NotificationTemplate.ACTIVE_30_DAYS).first()
                if not get_notification :      
                    @notify_when(events=[NotificationTemplate.ACTIVE_30_DAYS], is_route=False)
                    def notify(user, user_notifications):
                        """ extra logic if needed """
                    notify(user=current_user)    
        else:
            days_joined = self.since_join_days(current_user)
            if days_joined == 0:
                @notify_when(events=[NotificationTemplate.DAY1_JOINING],
                             is_route=False, is_one_time=True)
                def notify(user, user_notifications):
                    """ extra logic if needed """
                notify(user=current_user)
            elif days_joined >= 1:
                @notify_when(events=[NotificationTemplate.DAY2_JOINING],
                            is_route=False, is_one_time=True)
                def notify(user, user_notifications):
                    """ extra logic if needed """
                notify(user=current_user)

        return activity

