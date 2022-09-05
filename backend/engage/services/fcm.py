# coding: utf-8

from pyfcm import FCMNotification
from django.conf import settings

# engage modules
from . import _with

__all__ = (
    'FCM',
)


class FCM(object):
    push_service = FCMNotification(api_key=settings.FCM_SERVER_KEY)

    @classmethod
    @_with(log=True, threading=True)
    def single(cls, user, title, message, data=None, type='mobile'):
        cls.push_service.notify_single_device(
            registration_id=user.app_fcm_token or user.web_fcm_token or '',
            data_message={
                "title": title,
                "body": message
            }
        )

    @classmethod
    @_with(log=True, threading=True)
    def multiple(cls, users, title, message, data=None, type='mobile'):
        cls.push_service.notify_multiple_devices(
            registration_ids=[
                user.app_fcm_token or user.web_fcm_token or '' for user in users],
            data_message={
                "title": title,
                "body": message
            }
        )
