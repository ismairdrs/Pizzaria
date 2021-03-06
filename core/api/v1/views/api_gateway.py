from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from core.models import Api


class Gateway(APIView):
    permission_classes = (IsAuthenticated, )

    def operation(self, request):
        path = request.path_info.split('/')
        if len(path) < 2:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)

        api_model = Api.objects.filter(name=path[1])
        if api_model.count() != 1:
            return Response('Bad Request: Api não registrada', status=status.HTTP_400_BAD_REQUEST)

        response = api_model[0].send_request(request)
        data = self.try_convert_json(response)

        return Response(data=data, status=response.status_code)

    def get(self, request):
        return self.operation(request)

    def post(self, request):
        return self.operation(request)

    def put(self, request):
        return self.operation(request)

    def patch(self, request):
        return self.operation(request)

    def delete(self, request):
        return self.operation(request)

    def try_convert_json(self, res):
        try:
            return res.json()
        except:
            return {}
