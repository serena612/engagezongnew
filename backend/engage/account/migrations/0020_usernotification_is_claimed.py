# Generated by Django 3.2.7 on 2021-09-29 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotification',
            name='is_claimed',
            field=models.BooleanField(default=False),
        ),
    ]
