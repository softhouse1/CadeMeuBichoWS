from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404
from .Repositories import FuncoesDao

class Funcoes:
    def number_to_real(self, id):

        return 'R$ {:,.2f}'.format(float(id)).replace(',', 'v').replace('.', ',').replace('v', '.')

    def formata_valores(self, id):
        return '{:,.2f}'.format(float(id)).replace(',', 'v').replace('.', ',').replace('v', '.')

    @csrf_exempt
    def consulta_cidades_ibge(request):
        if request.method != 'POST': #or request.session['CodigoRetorno'] == 0:
            raise Http404

        fd = FuncoesDao()
        cidades = []
        if request.POST.get('Estado') != "0":
            cidades = fd.consulta_cidades_ibge(request.POST.get('Estado'))
        return JsonResponse({'Cidades':cidades})

    def consulta_estados_ibge(self):
        fd = FuncoesDao()
        estados = fd.consulta_estados_ibge(None)
        return JsonResponse({'Estados':estados})