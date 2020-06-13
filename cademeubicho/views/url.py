from django.urls import path
from .Usuario.Controller import *
from .PostAnimal.Controller import *
from .Login.Controller import *
from  .Funcoes.Controller import *
from .TipoAnimal.Controller import *
from .PorteAnimal.Controller import *

urlpatterns = [

    #AUTENTICACAO
    path('Login', Login.login),
    path('PrivacyPolicy', Login.privacidade),
    path('Apresentacao', Login.apresentacao),
    path('/', Login.apresentacao),

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
    path('TipoAnimal', TipoAnimal.tipo_animais),
    path('PorteAnimal', PorteAnimal.porte_animais),

]