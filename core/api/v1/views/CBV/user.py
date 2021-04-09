from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from rest_framework.views import APIView

from core.api.v1.serializer.user import UserSerializer
from core.models.usuario import User


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = {"users": serializer.data}
        return render(request, 'usuarios.html', data)


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = ''


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User


class UserDeleteView(DeleteView):
    model = User
