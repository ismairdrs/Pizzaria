from django.conf.urls import include, url
from django.urls import path

from .api import urls
from .api.v1.views import PizzaListView, PizzaCreateView, PizzaDetailView
from .api.v1.views.CBV.user import UserCreateView, UserDetailView, UserDeleteView, UserUpdateView

urlpatterns = [
    #url('q', include(urls)),
    path('pizza/', PizzaListView.as_view(), name='list_pizza'),
    path('nova-pizza/', PizzaCreateView.as_view(), name='new_pizza'),
    path('detalhe-pizza/<int:pk>', PizzaDetailView.as_view(), name='detail_pizza'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro', UserCreateView.as_view(), name='new_user'),
    path('usuario/<int:pk>', UserDetailView.as_view(), name='detail_user'),
    path('usuario/<int:pk>/delete', UserDeleteView.as_view(), name='delete-user'),
    path('usuario/<int:pk>/atualizar', UserUpdateView.as_view(), name='new_user'),
]
