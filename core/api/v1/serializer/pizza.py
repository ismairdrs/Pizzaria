from rest_framework import serializers

from core.api.v1.serializer.ingrediente import IngredienteSerializer
from core.models import Pizza, Ingrediente


class PizzaSerializer(serializers.ModelSerializer):

    ingrediente = IngredienteSerializer(read_only=True, many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'nome', 'codigo', 'ingrediente', 'preco')

