from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from core.rabbitmq import producer


class Likes(APIView):
    #permission_classes = (IsAuthenticated, )

    def post(self, request):
        body = self.valida_dados(request)
        if body:
            producer.produce(exchange='default', body=body, routing_key='celery')
            return Response({'Likes': 'like recebido'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Likes': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)

    def valida_dados(self, request):
        id_usuario = request.data.get('id_usuario')
        id_pizza = request.data.get('id_pizza')
        id_pedido = request.data.get('id_pedido')
        nota = request.data.get('nota')
        comentario = request.data.get('comentario') or ''

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
