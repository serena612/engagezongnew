# Generated by Django 3.2.6 on 2021-09-15 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0009_auto_20210904_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournamentprize',
            name='coins',
        ),
    ]
