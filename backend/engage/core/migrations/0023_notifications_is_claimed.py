# Generated by Django 3.2.7 on 2021-09-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210929_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='is_claimed',
            field=models.BooleanField(default=False),
        ),
    ]