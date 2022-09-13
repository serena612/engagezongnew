# Generated by Django 3.1.1 on 2022-04-12 10:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0036_auto_20220412_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='pool_prize',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='pool_prize_amount',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
