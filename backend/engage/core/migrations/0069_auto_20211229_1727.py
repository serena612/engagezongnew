# Generated by Django 3.2.7 on 2021-12-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_delete_gameapi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='coins',
        ),
        migrations.AddField(
            model_name='mission',
            name='free_user_coins',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mission',
            name='paid1_user_coins',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mission',
            name='paid2_user_coins',
            field=models.PositiveIntegerField(null=True),
        ),
    ]