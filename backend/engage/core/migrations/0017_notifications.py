# Generated by Django 3.2.7 on 2021-09-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_game_support_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('action', models.CharField(choices=[('popup', 'Popup'), ('video', 'Video'), ('redirect', 'Redirect'), ('text', 'Text')], default='text', max_length=20)),
                ('title', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='templates/')),
                ('template', models.CharField(blank=True, choices=[('home', 'Home Dashboard'), ('christmas', 'Christmas'), ('easter', 'Easter')], max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
