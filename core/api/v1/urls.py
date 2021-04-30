from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from core.api.v1.views.api_gateway import Gateway
from core.api.v1.views.likes import Likes
from core.api.v1.views.pizza import PizzaViewSet
from core.api.v1.views.token import TokenObtainPairView
from core.api.v1.views.usuario import UserViewSet


def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet, basename='pizza')
router.register('usuario', UserViewSet, basename='usuario')


urlpatterns = [
    path('sentry-debug/', trigger_error),
    url('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('avaliacao/', Likes.as_view(), name='avaliacao'),

    url(r'.*', Gateway.as_view()),
]
