from pydoc import cli
import requests
from celery import shared_task
from django.conf import settings
from django.db.models import F, OuterRef, Subquery
from django.utils import timezone
from engage.services import notify_when
from engage.account.models import UserGameLinkedAccount, User
from engage.core.constants import SupportedGame
from engage.tournament.game.clash_royale import ClashRoyaleClient
from engage.core.constants import NotificationTemplate


from engage.tournament.models import (
    TournamentMatch
)
from engage.account.models import User
from datetime import datetime, timedelta
@shared_task
def check_active_matches_winners():
    now = datetime.now(tz=timezone.utc)
    matches = TournamentMatch.objects.filter(
        start_date__gt=now,
        winners__isnull=True
    ).all()
    if len(matches) > 0 :
        for match in matches:
            fetch_match_details.delay(match.id)


@shared_task
def fetch_match_details(match_id):
    match = TournamentMatch.objects.get(
        id=match_id
    )
    now = datetime.now(tz=timezone.utc)
    started_date = (match.start_date  - now - timedelta(minutes=match.inform_participants))
    print(started_date.total_seconds())
    if int(started_date.total_seconds()) >=0  and  int(started_date.total_seconds()) < 30:
        participants = User.objects.filter(participanto=match)
        print("participants",participants)
        stri_repl = {}
        if match.start_date:
            if match.tournament.time_compared_to_gmt:               
                stri_repl['STARTDATE'] = (match.start_date+timedelta(hours=int(match.tournament.time_compared_to_gmt))).strftime("%H:%M")
            else:
                stri_repl['STARTDATE'] = match.start_date.strftime("%H:%M")
            if match.tournament.label_next_time:
                stri_repl['STARTDATE'] = stri_repl['STARTDATE'] + " " + match.tournament.label_next_time
        else:
            stri_repl['STARTDATE'] = ''
        stri_repl['MATCH_NAME'] = match.match_name
        stri_repl['TOURNAMENT_NAME'] = match.tournament.name
        stri_repl['NBR'] = str(match.inform_participants)
        stri_repl['GAMENAME'] = match.tournament.game.name
        stri_repl['MATCHID'] = str(match.match_id) if match.match_id else ''
        stri_repl['PASSWORD'] = match.password if match.password else ''

        
        print(participants)
        if len(participants) > 0 :
            for participant in participants :
                
                @notify_when(events=[NotificationTemplate.BEFORE_MATCH_INFORMATIVE], is_route=False, is_one_time=False, str_repl=stri_repl, lnk_repl="/tournaments/"+str(match.tournament.id))
                def notify(user,user_notifications):
                    """ extra logic if needed """
                    
                    for notificationi in user_notifications:
                        if match.start_date:
                            if match.tournament.label_next_time and match.tournament.time_compared_to_gmt:
                                date_time = (match.start_date+timedelta(hours=int(match.tournament.time_compared_to_gmt))).strftime("%H:%M") + " "+ match.tournament.label_next_time
                            else:
                                date_time = match.start_date.strftime("%H:%M")
                        else:
                            date_time = ''
                        print(notificationi.text)
                        notificationi.text=notificationi.notification.text.replace('MATCH_NAME',match.match_name).replace('TOURNAMENT_NAME',match.tournament.name).replace('NBR', str(match.inform_participants)).replace('GAMENAME',match.tournament.game.name).replace('MATCHID',str(match.match_id) if match.match_id else '').replace('PASSWORD',match.password if match.password else '').replace('STARTDATE',date_time)
                        print(notificationi.text)
                        notificationi.link = "/tournaments/"+str(match.tournament.id)  
                        notificationi.save()
                        print(notificationi.text)
                        print(notificationi.link)
        
                
                notify(user=participant)



    
 

# @shared_task
# def fetch_match_details(match_id):
#     match = TournamentMatch.objects.select_related(
#         'tournament',
#         'tournament__game',
#         'tournament__game__gameapi'
#     ).get(
#         id=match_id
#     )

#     game = match.tournament.game.support_game

#     client = None
#     if game == SupportedGame.CLASH_ROYALE:
#         client = ClashRoyaleClient(
#             token=settings.GAME_CLIENTS_TOKENS[SupportedGame.CLASH_ROYALE]
#         )
#     else:
#         return

#     tournament = client.retrieve_tournament(match.match_id)
#     if client :
#         winners = client.fetch_winners(
#             tournament,
#             tournament.tournamentprize_set.all().count()
#         )
#         user_game_account = UserGameLinkedAccount.objects.filter(
#             user=OuterRef('participant')
#         )
#         participants = match.tournament.tournamentparticipant_set.annotate(
#             game_account=Subquery(user_game_account.values('account')[:1])
#         ).all()
#         match.winners = ''
#         for participant in participants:
#             if client.is_winner(winners, participant.game_account):
#                 match.winners += f'{participant.participant.nickname}\n'

#     match.match_data = tournament
#     match.save()