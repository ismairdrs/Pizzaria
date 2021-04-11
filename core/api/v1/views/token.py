from rest_framework import serializers
from rest_framework_simplejwt.views import TokenViewBase

from core.api.v1.serializer.token import TokenObtainPairSerializer


class TokenObtainPairView(TokenViewBase):

    serializer_class = TokenObtainPairSerializer


token_obtain_pair = TokenObtainPairView.as_view()