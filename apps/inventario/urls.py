# Django

# Urls for the invetario app

from django.urls import path
from apps.inventario.views import *

urlpatterns = [
    path('', index, name='landingProgramas'),
]
