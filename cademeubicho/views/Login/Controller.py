from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.http.response import Http404
from django.views.decorators.csrf import csrf_exempt

from .Repositories import LoginDao
from cademeubicho.conexao import Conexao

class Login:

    @csrf_exempt
    def login(request):

        resul = []
        if request.POST:
            ld = LoginDao()
            param = {'UidFirebase': request.POST.get('uidFirebase') }
            param.update(request.POST.dict())

            resul = ld.get_usuario( param )
            print (resul)

            if resul == []:
                r = {
                    "nomeUsuario": "",
                    "numeroCelular": "",
                    "dddCelular": "",
                    "emailUsuario": "",
                    "distanciaFeed": 0,
                    "uidFirebase": ""
                }
                return JsonResponse(r, safe=False)
        else:
            raise Http404

        return JsonResponse(resul[0], safe=False)

