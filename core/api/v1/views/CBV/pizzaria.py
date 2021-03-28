from django.views import generic
from core.models import Pizza, Ingrediente


class PizzaListView(generic.ListView):
    model = Pizza


class PizzaDetailView(generic.DetailView):
    model = Pizza


class PizzaCreateView(generic.CreateView):
    model = Pizza
    fields = ['nome', 'codigo', 'tamanho', 'ingrediente', 'preco']

class PizzaDeleteView(generic.DeleteView):
    model = Pizza


class PizzaUpdateView(generic.UpdateView):
    model = Pizza


"""
    ingredientes
"""

class IngredienteListView(generic.ListView):
    model = Ingrediente


class IngredienteDetailView(generic.DetailView):
    model = Ingrediente


class IngredienteCreateView(generic.CreateView):
    model = Ingrediente


class IngredienteDeleteView(generic.DeleteView):
    model = Ingrediente


class IngredienteUpdateView(generic.UpdateView):
    model = Ingrediente
