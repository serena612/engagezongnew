# Generated by Django 3.2.7 on 2021-10-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20211007_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='template',
            field=models.CharField(choices=[('home', 'When User Reach Home Dashboard'), ('login', 'After User Login'), ('instant', 'Instant'), ('how_to_use', 'How To Use Engage'), ('invite', 'Invite & Earn Coins')], max_length=40, null=True),
        ),
    ]
