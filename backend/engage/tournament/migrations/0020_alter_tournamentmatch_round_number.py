# Generated by Django 3.2.7 on 2021-11-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0019_alter_tournament_give_sticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmatch',
            name='round_number',
            field=models.IntegerField(blank=True, choices=[('1', '1st Round'), ('2', '2nd Round'), ('3', '3rd Round'), ('4', '4th Round'), ('5', '5th Round'), ('6', '6th Round'), ('7', '7th Round'), ('8', '8th Round'), ('9', '9th Round'), ('10', '10th Round'), ('11', '11th Round'), ('12', '12th Round'), ('13', '13th Round'), ('14', '14th Round'), ('15', '15th Round'), ('16', '16th Round'), ('17', '17th Round'), ('18', '18th Round'), ('19', '19th Round'), ('20', '20th Round')], null=True),
        ),
    ]
