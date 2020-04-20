"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.urls import path, include

urlpatterns = [
    path('', include('webservice.views.Autenticacao.url')),
    path('', include('webservice.views.Cadastros.url')),
    path('', include('webservice.views.Funcoes.url')),
    path('', include('webservice.views.Consultas.url')),
]


