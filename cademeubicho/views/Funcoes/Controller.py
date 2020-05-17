from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from .Repositories import FuncoesDao

class Funcoes:
    def number_to_real(self, id):

        return 'R$ {:,.2f}'.format(float(id)).replace(',', 'v').replace('.', ',').replace('v', '.')

    def formata_valores(self, id):
        return '{:,.2f}'.format(float(id)).replace(',', 'v').replace('.', ',').replace('v', '.')
