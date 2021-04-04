from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.api.v1.serializer.pizza import PizzaSerializer
from core.models import Pizza
from core.rabbitmq import producer


class PizzaViewSet(viewsets.ModelViewSet):
    #queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):

        return Pizza.objects.all()