# Generated by Django 3.2.7 on 2021-11-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20211130_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='action',
            field=models.CharField(choices=[('popup', 'Popup'), ('video', 'Video'), ('redirect', 'Redirect'), ('text', 'Text'), ('event', 'Event')], default='text', max_length=20),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='template',
            field=models.CharField(choices=[('instant', 'Instant One Time'), ('send_coins', 'Send Coins'), ('daily', 'Daily'), ('once_a_month', 'One A Month'), ('home', 'When User Reach Home Dashboard'), ('login', 'After User Login'), ('how_to_use', 'How To Use Engage'), ('active_5_days', '5 Active Days After Joining'), ('active_10_days', '10 Active Days After Joining'), ('active_30_days', '30 Active Days After Joining'), ('user_register_for_tournament', 'User Registers For A Tournament'), ('user_first_tournament', 'User Who Is First In Any Tournament'), ('user_second_third_tournament', 'Users Who Win A Prize (2nd and more)'), ('user_outside_the_winning_positions', 'User Outside The Winning Positions'), ('happy_birthday', 'Happy Birthday'), ('friend_added', 'Friend Added'), ('friend_remove', 'Friend Remove'), ('friend_request', 'Friend Request'), ('video_added', 'New Video Added'), ('user_watch_video', 'If User Watches Any Video'), ('holiday', 'Holiday')], max_length=40, null=True),
        ),
    ]
