from django.conf.urls import include, url
from django.urls import path

from .api import urls
from .api.v1.views import PizzaListView, PizzaCreateView, PizzaDetailView

urlpatterns = [
    url('api/', include(urls)),
    path('', PizzaListView.as_view(), name='pizza-list'),
    path('nova-pizza/', PizzaCreateView.as_view(), name='nova-pizza'),
    path('detalhe-pizza/<int:pk>/', PizzaDetailView.as_view(), name='detail-pizza')
]