from django.conf.urls import include, url
from django.urls import path

from .api import urls
from .api.v1.views import PizzaListView, PizzaCreateView, PizzaDetailView

urlpatterns = [
    url('', include(urls)),
]
