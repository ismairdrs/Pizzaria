from django.conf.urls import include, url

from .api import urls

urlpatterns = [
    url('', include(urls)),
]
