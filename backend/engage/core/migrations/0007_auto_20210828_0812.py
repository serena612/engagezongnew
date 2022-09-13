# Generated by Django 3.2.6 on 2021-08-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_gameapi_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='average_game_duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actioncoin',
            name='action',
            field=models.CharField(choices=[('sign_up', 'On Sign Up'), ('ad_watch', 'On Ad Watch'), ('win_match', 'On Match Win'), ('win_tournament', 'On Tournament Win')], max_length=64, unique=True),
        ),
    ]