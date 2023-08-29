# Generated by Django 3.2.7 on 2021-10-06 02:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20211003_0540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='battlepass',
            options={'verbose_name': 'Battle Pass', 'verbose_name_plural': 'Battle Pass'},
        ),
        migrations.AddField(
            model_name='notifications',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]