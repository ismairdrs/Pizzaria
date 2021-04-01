from django.shortcuts import render
from rest_framework.views import APIView

from core.api.v1.serializer.user import UserSerializer
from core.models.usuario import User


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = {"users": serializer.data}
        return render(request, 'usuarios.html', data)
