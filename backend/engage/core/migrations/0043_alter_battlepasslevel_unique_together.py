# Generated by Django 3.2.7 on 2021-10-13 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20211011_1435'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='battlepasslevel',
            unique_together={('battle_pass', 'level')},
        ),
    ]
