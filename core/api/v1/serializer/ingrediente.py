from rest_framework import serializers

from core.models import Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        fields = ('id', 'nome', 'descricao')
