# Generated by Django 3.1.1 on 2022-05-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0040_auto_20220505_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='time_compared_to_gmt',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Time compared to GMT (+ or -)'),
        ),
    ]
