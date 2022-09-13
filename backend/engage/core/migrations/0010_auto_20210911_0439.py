# Generated by Django 3.2.6 on 2021-09-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210911_0314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuration',
            options={'verbose_name_plural': 'Configuration'},
        ),
        migrations.AddField(
            model_name='configuration',
            name='a_party_invitation_free_day',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='configuration',
            name='a_party_invitation_level',
            field=models.PositiveIntegerField(default=1, help_text='increase level'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='a_party_invitation_reward',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AddField(
            model_name='configuration',
            name='b_party_invitation_free_day',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='configuration',
            name='b_party_invitation_level',
            field=models.PositiveIntegerField(default=0, help_text='increase level'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='b_party_invitation_reward',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
