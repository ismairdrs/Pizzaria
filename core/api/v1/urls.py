from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from core.api.v1.views.CBV.user import UserAPIView
from core.api.v1.views.ingrediente import IngredienteViewSet
from core.api.v1.views.pizza import PizzaViewSet
from core.api.v1.views.usuario import UserViewSet

router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet, basename='pizza')
router.register('ingrediente', IngredienteViewSet, basename='ingrediente')
router.register('usuario', UserViewSet, basename='usuario')

urlpatterns = [
    url('', include(router.urls)),
]
