# Generated by Django 3.1.1 on 2022-01-19 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_auto_20220119_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredgame',
            name='nbr_of_coins',
        ),
    ]
