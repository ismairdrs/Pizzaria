from django.contrib.postgres.fields import ArrayField
from django.db import models

# classe que define um 'modelo' de pizza que será vendida na pizzaria
from core.models import Ingrediente


class Pizza(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)
    ingrediente = models.ManyToManyField(Ingrediente, related_name='ingrediente', verbose_name='ingrediente')
    preco = models.DecimalField(verbose_name='preco', decimal_places=2, max_digits=5)
    descricao = models.TextField(blank=True)

