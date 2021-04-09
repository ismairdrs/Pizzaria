from django.conf.urls import include, url
from django.urls import path

from .api import urls
from .api.v1.views import PizzaListView, PizzaCreateView, PizzaDetailView

urlpatterns = [
    #url('q', include(urls)),
    path('pizza/', PizzaListView.as_view(), name='list_pizza'),
    path('nova-pizza/', PizzaCreateView.as_view(), name='new_pizza'),
    path('detalhe-pizza/<int:pk>', PizzaDetailView.as_view(), name='detail_pizza'),
]
