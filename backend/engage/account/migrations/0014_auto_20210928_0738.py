# Generated by Django 3.2.7 on 2021-09-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20210927_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernotification',
            name='notification',
        ),
        migrations.AddField(
            model_name='usernotification',
            name='action',
            field=models.CharField(choices=[('popup', 'Popup'), ('video', 'Video'), ('redirect', 'Redirect'), ('text', 'Text')], default='text', max_length=20),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='template',
            field=models.CharField(blank=True, choices=[('christmas', 'Christmas'), ('easter', 'Easter')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]