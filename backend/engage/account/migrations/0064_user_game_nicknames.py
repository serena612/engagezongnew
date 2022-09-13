# Generated by Django 3.1.1 on 2022-03-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0063_auto_20220306_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='game_nicknames',
            field=models.ManyToManyField(blank=True, related_name='_user_game_nicknames_+', to='account.UserGameNicknames'),
        ),
    ]
