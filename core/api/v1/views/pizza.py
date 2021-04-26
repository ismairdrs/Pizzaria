from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.api.v1.serializer.pizza import PizzaSerializer
from core.models import Pizza


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(PizzaViewSet, self).get_permissions()
