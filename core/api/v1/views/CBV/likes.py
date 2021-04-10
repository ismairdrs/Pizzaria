import requests
from django.shortcuts import render


def cadastrar_avaliacao(request):
    def post(request):
        requests.post('http://127.0.0.1:8000/likes/', )
    return render(request, 'core/likes.html')