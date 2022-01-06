from django.urls import path
from django.conf.urls import url
from .api import (
    getServices,
    getHistory
)
urlpatterns = [
    path('getServices',getServices , name='getServices'),
    path('getHistory',getHistory , name='getHistory'),

]