from rest_framework import serializers

from core.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('id', 'nome', 'codigo', 'ingrediente', 'preco', 'descricao', )

