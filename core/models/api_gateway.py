import json

import requests
from django.db import models


class Api(models.Model):
    # nome do serviço (api) a ser consultado
    name = models.CharField(max_length=128, unique=True)
    # identificaçao no uri que leva ao serviço /user/ /likes/ /pizza/
    request_path = models.CharField(max_length=255, unique=True)
    # endereço da api http://127.0.0.1:8000/
    upstream_url = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def send_request(self, request):
        headers = {}
        strip = '' + self.request_path
        full_path = request.get_full_path()[len(strip):]
        url = self.upstream_url + full_path
        method = request.method.lower()
        method_map = {
            'get': requests.get,
            'post': requests.post,
            'put': requests.put,
            'patch': requests.patch,
            'delete': requests.delete
        }

        if request.content_type and request.content_type.lower() == 'application/json':
            data = json.dumps(request.data)
            headers['content-type'] = request.content_type
        else:
            data = request.data

        return method_map[method](url, headers=headers, data=data, files=request.FILES)

    def __str__(self):
        return self.name
