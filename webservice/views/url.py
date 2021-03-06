from django.urls import path
from .Usuario.Controller import *
from .PostAnimal.Controller import *
from .Login.Controller import *
from  .Funcoes.Controller import *
from .TipoAnimal.Controller import *
from .PorteAnimal.Controller import *
from .Temporario.Controller import *

urlpatterns = [
    # URL TEMPORARIA - SERÁ RETIRADA
    path('UsuariosSistema', Temporario.get_usuarios),
    path('PostSistema', Temporario.get_posts),
    path('PostResumido', Temporario.get_posts_completo),


    #AUTENTICACAO
    path('Login', Login.login),

    # USUARIO
    path('CadastrarUsuario', Usuario.cadastra_usuario),
    path('AtualizarUsuario', Usuario.atualiza_usuario),

    #POST
    path('CadastrarPost', PostAnimal.cadastra_post_animal),
    path('AtualizarPost', PostAnimal.atualiza_post_animal),
    path('DesativarPost', PostAnimal.desativa_post),

    #POST CONSULTA
    path('PostsProximos', PostAnimal.get_posts_proximos),
    path('MeusPosts', PostAnimal.get_posts_usuario),


    #FUNCOES / SELECT
    path('ConsultaCidadesIbge', Funcoes.consulta_cidades_ibge),
    path('ConsultaEstadosIbge', Funcoes.consulta_estados_ibge),
    path('TipoAnimal', TipoAnimal.tipo_animais),
    path('PorteAnimal', PorteAnimal.porte_animais),

]