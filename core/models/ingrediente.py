from django.db import models

# não sei se precisa mesmo dessa classe


class Ingrediente(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
