# Generated by Django 3.2.7 on 2021-12-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0046_auto_20211213_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_seen',
        ),
        migrations.AddField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]