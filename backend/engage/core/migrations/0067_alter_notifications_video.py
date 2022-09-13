# Generated by Django 3.2.7 on 2021-12-17 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_alter_notifications_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='video',
            field=models.FileField(blank=True, help_text='MOV, mp4 or webm supported', null=True, upload_to='videos_uploaded/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm'])]),
        ),
    ]
