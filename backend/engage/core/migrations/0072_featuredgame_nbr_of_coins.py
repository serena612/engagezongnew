# Generated by Django 3.1.1 on 2022-01-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20220110_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredgame',
            name='nbr_of_coins',
            field=models.PositiveIntegerField(default=10),
        ),
    ]