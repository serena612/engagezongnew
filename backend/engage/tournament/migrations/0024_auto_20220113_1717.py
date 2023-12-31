# Generated by Django 3.1.1 on 2022-01-13 15:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0023_auto_20220110_1159'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tournamentprize',
            unique_together={('tournament', 'winner'), ('tournament', 'position')},
        ),
        migrations.RemoveField(
            model_name='tournamentprize',
            name='category',
        ),
    ]
