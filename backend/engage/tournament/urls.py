from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import api
from . import views

router = SimpleRouter()
router.register('tournaments', api.TournamentViewSet)
router.register('tournaments-prizes', api.TournamentPrizeViewSet)
router.register('winners', api.TournamentWinnerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('tournaments/<str:slug>/', views.tournament_view,
         name='tournament-page'),
]
