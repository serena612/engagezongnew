# Generated by Django 3.2.7 on 2022-08-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_auto_20220804_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='package',
            field=models.ManyToManyField(null=True, to='core.Package', verbose_name='Package'),
        ),
    ]
