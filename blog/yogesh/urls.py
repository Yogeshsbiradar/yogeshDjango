from django.conf.urls import url
from .views import yogeshblog


urlpatterns = [
    url(r'^$',yogeshblog,name='yogeshblog')
]