# Generated by Django 3.1.1 on 2022-01-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_remove_featuredgame_nbr_of_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredgame',
            name='nbr_of_coins',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
