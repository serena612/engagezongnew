# Generated by Django 3.2.6 on 2021-09-11 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_coins'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('last_read', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
