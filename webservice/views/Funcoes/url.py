from django.urls import path

from ..Funcoes.Controller import *



urlpatterns = [
    path('ConsultaCidadesIbge', Funcoes.consulta_cidades_ibge),
    path('ConsultaEstadosIbge', Funcoes.consulta_estados_ibge),

]