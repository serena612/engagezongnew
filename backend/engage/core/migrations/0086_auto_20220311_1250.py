# Generated by Django 3.1.1 on 2022-03-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_auto_20220306_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='package',
            field=models.ManyToManyField(to='core.Package', verbose_name='Package'),
        ),
    ]
