from django.urls import path
from .Usuario.Controller  import *
from .PostAnimal.Controller  import *

urlpatterns = [

    # USUARIO
    path('CadastrarUsuario', Usuario.cadastra_usuario),
    path('AtualizarUsuario', Usuario.atualiza_usuario),

    #POST
    path('CadastrarPost', PostAnimal.cadastra_post_animal),
    path('AtualizarPost', PostAnimal.atualiza_post_animal),
    path('DesativarPost', PostAnimal.desativa_post),

    path('PostsProximos', PostAnimal.get_posts_proximos),
    path('MeusPosts', PostAnimal.get_posts_usuario),

]