from django.conf.urls import include, url
from django.urls import path

from .api import urls
from .api.v1.views import PizzaListView, PizzaCreateView, PizzaDetailView
from .api.v1.views.CBV.likes import cadastrar_avaliacao

from .api.v1.views.CBV.user import UserCreateView, UserDetailView, UserDeleteView, UserUpdateView

urlpatterns = [
    url('', include(urls)),
]
