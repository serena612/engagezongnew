# Generated by Django 3.2.7 on 2021-11-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_alter_game_support_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='html5game',
            name='game_type',
            field=models.CharField(choices=[('free', 'Free Game'), ('premium', 'Premium Game'), ('exclusive', 'Exclusive Game')], max_length=12, null=True),
        ),
    ]
