from django.contrib import admin

from core.models import Pizza, Api, User


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'preco')


@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
    pass

admin.register(User)