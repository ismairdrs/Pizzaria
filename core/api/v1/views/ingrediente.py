from rest_framework import viewsets

from core.api.v1.serializer.ingrediente import IngredienteSerializer
from core.models import Ingrediente


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
