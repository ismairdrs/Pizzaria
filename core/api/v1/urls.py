from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from core.api.v1.views.api_gateway import Gateway
from core.api.v1.views.likes import Likes
from core.api.v1.views.pizza import PizzaViewSet
from core.api.v1.views.usuario import UserViewSet

from rest_framework_simplejwt import views as jwt_views



router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet, basename='pizza')
router.register('usuario', UserViewSet, basename='usuario')


urlpatterns = [
    url('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('likes/', Likes.as_view(), name='likes'),
    url(r'.*', Gateway.as_view()),
]
