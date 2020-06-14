from django.http import JsonResponse
from .Repositories import PorteAnimalDao

class PorteAnimal:

    def porte_animais(request):
        ld = PorteAnimalDao()
        t = ld.busca_porte()
        return JsonResponse({'PorteAnimal': t})


