# Generated by Django 3.2.7 on 2021-09-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_html5game_game_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='game',
            name='mobile_link',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='pc_link',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
