from rest_framework import viewsets

from core.api.v1.serializer.pizza import PizzaSerializer
from core.models import Pizza


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
