# Generated by Django 3.2.7 on 2021-10-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0033_alter_friendlist_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotification',
            name='friend_uid',
            field=models.TextField(blank=True, null=True),
        ),
    ]