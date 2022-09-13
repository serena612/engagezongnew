# Generated by Django 3.2.7 on 2021-10-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_auto_20211025_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='discord',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitch',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website',
        ),
        migrations.AddField(
            model_name='profile',
            name='residency',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
