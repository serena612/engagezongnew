from django.utils import timezone
from django.contrib.auth.models import UserManager


class BattlePassManager(UserManager):

    def get_active(self):
        now = timezone.now()
        return self.get_queryset().filter(
            starts_at__lte=now,
            ends_at__gt=now,
            is_active=True
        )
