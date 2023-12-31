# Generated by Django 3.1.1 on 2022-05-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0039_auto_20220419_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='live_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='top_image',
            field=models.ImageField(null=True, upload_to='tournaments/', verbose_name='Detail Image'),
        ),
    ]
