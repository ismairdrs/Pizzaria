from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase

from core.api.v1.serializer.token import TokenObtainPairSerializer


class TokenObtainPairView(TokenViewBase):

    serializer_class = TokenObtainPairSerializer


token_obtain_pair = TokenObtainPairView.as_view()


class ValidarToken(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={'token': 'valido'}, status=200)
