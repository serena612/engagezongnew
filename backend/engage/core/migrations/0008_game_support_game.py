# Generated by Django 3.2.6 on 2021-09-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210828_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='support_game',
            field=models.CharField(choices=[('dota2', 'Dota 2'), ('clash_royal', 'Clash Royal')], max_length=32, null=True),
        ),
    ]
