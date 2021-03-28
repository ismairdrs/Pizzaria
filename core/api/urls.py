from django.conf.urls import include, url

from .v1 import urls

urlpatterns = [
    url('v1/', include(urls)),
]