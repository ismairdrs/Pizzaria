from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from core.rabbitmq import Producer



class Likes(APIView):
    #permission_classes = (IsAuthenticated, )

    def post(self, request):
        body = self.valida_dados(request)
        if body:
            producer = Producer()
            producer.produce(exchange='likes', body=body, routing_key='likes')
            producer.close_connection()
            return Response({'Likes': 'like recebido'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Likes': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)

    def valida_dados(self, request):
        id_usuario = request.data.get('id_usuario')
        id_pizza = request.data.get('id_pizza')
        id_pedido = request.data.get('id_pedido')
        nota = request.data.get('nota')
        comentario = request.data.get('comentario') or ''
        if 0 <= nota <= 5:
            True
        else:
            return False
        if id_usuario and id_pizza and id_pedido and nota and comentario:
            body = {
                "id_usuario": id_usuario,
                "id_pizza": id_pizza,
                "id_pedido": id_pedido,
                "nota": nota,
                "comentario": comentario,
            }
            return body
        else:
            return False
