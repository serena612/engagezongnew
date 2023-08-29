from django.db.models import F, Prefetch
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import  timedelta
from engage.account.constants import SubscriptionPlan
from engage.tournament.models import Tournament, TournamentParticipant, TournamentPrize


def tournament_view(request, slug):
    user = request.user

    now = timezone.now()
    try:
        tournament = Tournament.objects.select_related(
            'game',
        ).prefetch_related(
            'tournamentparticipant_set',
            Prefetch(
                'tournamentprize_set',
                queryset=TournamentPrize.objects.order_by('position')
            ),
        ).annotate(
            starts_in=F('start_date') - now
        ).get(
            slug=slug,
            regions__in=[request.region]
        )
    except Tournament.DoesNotExist:
        #if slug has been changed get by id

        try:
            tournament = Tournament.objects.select_related(
                'game',
            ).prefetch_related(
                'tournamentparticipant_set',
                Prefetch(
                    'tournamentprize_set',
                    queryset=TournamentPrize.objects.order_by('position')
                ),
            ).annotate(
                starts_in=F('start_date') - now
            ).get(
                id=slug,
                regions__in=[request.region]
            )
        except Tournament.DoesNotExist:
            #if slug has been changed get by id
            return redirect('/')

    participant = None
    if user.is_authenticated:
        participant = tournament.get_participant(user)

    can_join = True
    if user.is_authenticated and user.subscription == SubscriptionPlan.PAID1:
        can_join = not TournamentParticipant.objects.filter(
            tournament__regions__in=[request.region],
            participant=user,
            created__date=now.date()
        ).exists()
    if user.is_authenticated :
        game_account = tournament.game.usergamelinkedaccount_set.filter(user=user).last()
    else :
        game_account = tournament.game.usergamelinkedaccount_set.last()   
    
    now = timezone.now()
    starts_in = tournament.start_date - now
    if starts_in.days :
        starts_in_full = f'{starts_in.days} days, {int(starts_in.seconds // 3600)} hours and {int((starts_in.seconds // 60) % 60)} minutes'
    else:
        starts_in_full = f'{int(starts_in.seconds // 3600)} hours and {int((starts_in.seconds // 60) % 60)} minutes'
    
    tournament_started = tournament.start_date
    if tournament.time_compared_to_gmt and '+' in tournament.time_compared_to_gmt :
        tournament_started = tournament.start_date + timedelta(hours=int(tournament.time_compared_to_gmt))
    if tournament.time_compared_to_gmt and '-' in tournament.time_compared_to_gmt :
        tournament_started = tournament.start_date - timedelta(hours=int(tournament.time_compared_to_gmt))


    return render(request, 'tournament.html', {'tournament': tournament,
                                               'user': user,
                                               'starts_in_full': starts_in_full,
                                               'game_account': game_account,
                                               'tournament_started': tournament_started,
                                               'participant': participant,
                                               'can_join': can_join,
                                               'currentDate':now})
