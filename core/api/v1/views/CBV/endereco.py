from rest_framework.views import APIView


class EnderecoAPIView(APIView):

    def post(self):
        #cadastra um endereço para o usuário na outra API
        pass

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = {"users": serializer.data}
        return render(request, 'usuarios.html', data)