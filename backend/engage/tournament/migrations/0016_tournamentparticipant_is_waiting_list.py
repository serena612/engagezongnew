# Generated by Django 3.2.7 on 2021-11-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0015_auto_20211031_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentparticipant',
            name='is_waiting_list',
            field=models.BooleanField(default=False),
        ),
    ]