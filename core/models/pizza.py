from django.contrib.postgres.fields import ArrayField
from django.db import models

# classe que define um 'modelo' de pizza que será vendida na pizzaria



class Pizza(models.Model):
    nome = models.CharField(max_length=255)
    ingrediente = models.TextField()
    preco = models.DecimalField(verbose_name='preco', decimal_places=2, max_digits=5)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

