# Generated by Django 3.1.1 on 2022-04-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0068_usernotification_is_popup'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_billed',
            field=models.BooleanField(default=False),
        ),
    ]
