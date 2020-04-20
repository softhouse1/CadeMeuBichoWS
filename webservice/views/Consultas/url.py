from django.urls import path
from .TipoAnimal.Controller import *
from .PorteAnimal.Controller import *

urlpatterns = [
    path('TipoAnimal', TipoAnimal.tipo_animais),
    path('PorteAnimal', PorteAnimal.porte_animais),
]