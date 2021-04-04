from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.models.usuario import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = User(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario
