from rest_framework import serializers

from core.models.usuario import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
