# Generated by Django 3.2.7 on 2021-10-11 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_battlepass_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='mission',
            name='last_active',
        ),
    ]