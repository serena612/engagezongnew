# Generated by Django 3.2.7 on 2021-10-31 18:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournament', '0014_tournamentprize_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentprize',
            name='category',
            field=models.CharField(choices=[('free', 'Free'), ('subscribe', 'Subscriber')], max_length=10, null=True, verbose_name='Winner Category'),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentprize',
            unique_together={('tournament', 'winner'), ('tournament', 'category', 'position')},
        ),
    ]