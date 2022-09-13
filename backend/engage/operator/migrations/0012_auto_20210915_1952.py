# Generated by Django 3.2.6 on 2021-09-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operator', '0011_operatorad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operatorwebsite',
            name='home_page_video',
        ),
        migrations.AddField(
            model_name='operatorad',
            name='operators',
            field=models.ManyToManyField(to='operator.Operator'),
        ),
        migrations.DeleteModel(
            name='OperatorConfiguration',
        ),
    ]
