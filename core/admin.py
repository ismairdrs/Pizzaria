from django.contrib import admin

from core.models import Pizza, Ingrediente


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'tamanho', 'preco')


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
