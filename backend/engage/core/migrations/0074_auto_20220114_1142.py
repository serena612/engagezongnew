# Generated by Django 3.1.1 on 2022-01-14 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_game_rules'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='rules',
            new_name='general_rules',
        ),
    ]
