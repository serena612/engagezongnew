# Generated by Django 3.2.7 on 2021-12-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0049_auto_20211229_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertransactionhistory',
            name='actual_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usertransactionhistory',
            name='action',
            field=models.CharField(choices=[('add', 'Add'), ('buy', 'Buy'), ('send', 'Send'), ('receive', 'Receive'), ('redeem', 'Redeem')], default='add', max_length=12),
        ),
    ]
