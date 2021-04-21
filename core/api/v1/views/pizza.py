from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.api.v1.serializer.pizza import PizzaSerializer
from core.models import Pizza


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    #permission_classes = (IsAuthenticated, IsAdminUser)
