# Generated by Django 3.1.1 on 2022-03-06 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0062_user_game_nicknames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='game_nicknames',
        ),
        migrations.CreateModel(
            name='UserGameNicknames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('game_nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.usergamelinkedaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Game Nicknames',
                'unique_together': {('user', 'game_nickname')},
            },
        ),
    ]
