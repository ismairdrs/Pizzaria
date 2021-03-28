from django.contrib.postgres.fields import ArrayField
from django.db import models

# classe que define um 'modelo' de pizza que será vendida na pizzaria
from core.models import Ingrediente


class Pizza(models.Model):
    CHOICES = (
        ('p','PEQUENA'),('m', 'MEDIA'), ('g','GRANDE')
    )
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)
    tamanho = models.CharField(choices=CHOICES, max_length=7,)
    ingrediente = models.ManyToManyField(Ingrediente, related_name='ingrediente', verbose_name='ingrediente')
    preco = models.DecimalField(verbose_name='preco', decimal_places=2, max_digits=5)


    def get_absolute_url(self):
        return ''