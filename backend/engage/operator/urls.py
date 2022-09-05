from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from . import api


router = SimpleRouter()
router.register('regions', api.RegionViewSet)
router.register('orders', api.OrderViewSet, basename='orders')


urlpatterns = [
    path('api/', include(router.urls))
]
