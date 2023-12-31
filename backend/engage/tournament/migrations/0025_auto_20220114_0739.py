# Generated by Django 3.2.7 on 2022-01-14 07:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0024_auto_20220112_0900'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tournamentprize',
            unique_together={('tournament', 'position'), ('tournament', 'winner')},
        ),
        migrations.RemoveField(
            model_name='tournamentprize',
            name='category',
        ),
    ]
