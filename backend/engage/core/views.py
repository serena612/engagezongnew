from django.db.models import F, Q,Prefetch
from django.http import HttpResponse, Http404,HttpResponseForbidden
from django.shortcuts import render, redirect
from django.utils import timezone
from engage.tournament.models import Tournament,TournamentPrize


from engage.core.models import HTML5Game, Event, FeaturedGame, Game
from engage.core.constants import NotificationTemplate
from engage.operator.models import OperatorAd
from engage.services import notify_when


@notify_when(events=[
    NotificationTemplate.HOME,
    NotificationTemplate.HOW_TO_USE
])
def home_view(request):
    now = timezone.now()
    featured_games = FeaturedGame.objects.all()
    games = Game.objects.all()
    ad = OperatorAd.objects.filter(
        (Q(start_date__gte=now) & Q(end_date__lte=now)) |
        (Q(start_date__isnull=True) & Q(end_date__isnull=True)),
        regions__in=[request.region]
    ).order_by('?').first()
    events = Event.objects.filter(
        regions__in=[request.region]
    ).all().order_by('?')[:20]

    previous_tournaments = Tournament.objects.select_related('game').prefetch_related(
        'tournamentparticipant_set',
        Prefetch(
            'tournamentprize_set',
            queryset=TournamentPrize.objects.order_by('position')
        )
    ).filter(regions__in=[request.region],end_date__lt=now).order_by('name')
    return render(request, 'index.html', {'featured_games': featured_games,
                                          'games': games,
                                          'ad': ad,
                                          'events': events,
                                          'previous_tournaments':previous_tournaments})


def about_view(request):
    return render(request, 'about.html', {})


## TODO: to handle header enrichment here
def register_view(request):
    if request.user and request.user.is_authenticated :
       return redirect('/')
    else :
       print(request.headers)
       return render(request, 'register.html', {'wifi':True})

def new_register_view(request):
    if request.user and request.user.is_authenticated :
        return redirect('/')
    else :
        return render(request, 'register1.html', {})

def faq_view(request):
    return render(request, 'FAQ.html', {})


def terms_view(request):
    return render(request, 'terms.html', {})


def privacy_view(request):
    return render(request, 'privacy.html', {})


def disclaimer_view(request):
    return render(request, 'disclaimer.html', {})


def html5_game_view(request, game):
    try:
        html5_game = HTML5Game.objects.filter(
            regions__in=[request.region]
        ).get(slug__iexact=game)
    except HTML5Game.DoesNotExist:
        raise Http404

    return redirect(f'/html5_game/{html5_game.slug}/')


def firebase_sw_view(request):
    return HttpResponse("""
        importScripts('https://www.gstatic.com/firebasejs/9.1.1/firebase-app-compat.js');
        importScripts('https://www.gstatic.com/firebasejs/9.1.1/firebase-messaging-compat.js');
        

        firebase.initializeApp({
            apiKey: "AIzaSyA0HHeMbJieI4Qp5tyxn765mk0IWllTCco",
            authDomain: "engageplaywin-ced7f.firebaseapp.com",
            projectId: "engageplaywin-ced7f",
            storageBucket: "engageplaywin-ced7f.appspot.com",
            messagingSenderId: "615474016768",
            appId: "1:615474016768:web:7cfa190a078416cc3a9ee5",
            measurementId: "G-4FTX1VRLYN"
        });

        const messaging = firebase.messaging();

       
    """, status=200, content_type='application/javascript')


def view_404(request, exception=None): 
    return redirect('/')


# def error_403(request, exception):
#         return render(request,'403.html') 