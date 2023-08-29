from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import WinAction
from .models import BattlePass, Mission, BattlePassMission
from .utils import daterange


@receiver(post_save, sender=BattlePass)
def new_battle_pass(sender, instance, created, **kwargs):
    if created:
        missions = Mission.objects.filter(action__in=WinAction.values).all()
        bp_missions = []
        for k, single_date in enumerate(daterange(instance.starts_at,
                                                  instance.ends_at)):
            mission = missions[k % len(missions)]
            bp_missions.append(BattlePassMission(
                battle_pass=instance,
                mission=mission,
                date=single_date
            ))
        BattlePassMission.objects.bulk_create(bp_missions)
