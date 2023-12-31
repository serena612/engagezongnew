# Generated by Django 3.2.7 on 2021-11-30 15:29

from django.db import migrations, models
import engage.core.managers


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_event_regions'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='battlepass',
            managers=[
                ('objects', engage.core.managers.BattlePassManager()),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='claim_instantly',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='action',
            field=models.CharField(choices=[('popup', 'Popup'), ('video', 'Video'), ('redirect', 'Redirect'), ('text', 'Text')], default='text', max_length=20),
        ),
    ]
