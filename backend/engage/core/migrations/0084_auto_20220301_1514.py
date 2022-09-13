# Generated by Django 3.1.1 on 2022-03-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_auto_20220228_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='is_popup',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='subscription',
        ),
        migrations.AddField(
            model_name='notifications',
            name='is_popup',
            field=models.BooleanField(default=False, verbose_name='display as popup'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='package',
            field=models.ManyToManyField(blank=True, to='core.Package', verbose_name='Send to'),
        ),
    ]
