from django.views import generic
from core.models import Pizza


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
