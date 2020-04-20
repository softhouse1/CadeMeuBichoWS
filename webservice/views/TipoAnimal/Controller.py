from django.http import JsonResponse
from .Repositories import TipoAnimalDao

class TipoAnimal:

    def tipo_animais(request):
        ld = TipoAnimalDao()
        t = ld.busca_tipos()
        return JsonResponse({'TiposAnimal': t})


