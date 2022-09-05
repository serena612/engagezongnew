from django.conf import settings

from engage.account.models import UserNotification
from engage.core.constants import UserProfileStates

# TODO: needs refactoring, data must be generated in the frontend
days = [f'{day}' if day > 9 else f'0{day}' for day in range(1, 32)]
years = [f'{year}' for year in range(1930, 2013)]


def notifications(request):
    return {
        'notifications': UserNotification.objects.filter(
            user=request.user,
            last_read__isnull=True
        ).count() if request.user.is_authenticated else 0
    }


def profile_states(request):
    return {'states': UserProfileStates}


def date_picker(request):
    return {
        'days': days,
        'years': years
    }


def fcm_api_config(request):
    return {
        'fcm_config': {
            'apiKey': settings.FCM_CONFIG.get('apiKey'),
            'authDomain': settings.FCM_CONFIG.get('authDomain'),
            'projectId': settings.FCM_CONFIG.get('projectId'),
            'storageBucket': settings.FCM_CONFIG.get('storageBucket'),
            'messagingSenderId': settings.FCM_CONFIG.get('messagingSenderId'),
            'appId': settings.FCM_CONFIG.get('appId'),
            'measurementId': settings.FCM_CONFIG.get('measurementId'),
        }
    }