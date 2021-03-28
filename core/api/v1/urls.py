from django.conf.urls import url, include
from rest_framework import routers

from core.api.v1.views.pizza import PizzaViewSet

router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet, basename='pizza')

urlpatterns = [
    url('', include(router.urls)),

]
