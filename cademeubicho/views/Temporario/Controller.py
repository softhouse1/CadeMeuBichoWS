from django.http import JsonResponse
from .Repositories import TempDao

class Temporario:

    def get_usuarios(request):
        temp = TempDao()
        t = temp.busca_usuarios()
        return JsonResponse({'Usuarios': t})

    def get_posts(request):
        temp = TempDao()
        t = temp.busca_posts()
        return JsonResponse({'Posts': t})

    def get_posts_completo(request):
        temp = TempDao()
        t = temp.busca_posts_completo()
        return JsonResponse({'Posts': t})
