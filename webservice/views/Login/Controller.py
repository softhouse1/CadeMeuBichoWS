from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.http.response import Http404
from django.views.decorators.csrf import csrf_exempt

from .Repositories import LoginDao
from CadeMeuBicho.webservice.conexao import Conexao

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

            if resul != []:
                resul = resul[0]
                request.session['nomeUsuario'] = resul['nomeUsuario']
                request.session['numeroCelular'] = resul['numeroCelular']
                request.session['dddCelular'] = resul['dddCelular']
                request.session['emailUsuario'] = resul['emailUsuario']
                request.session['ufUsuario'] = resul['ufUsuario']
                request.session['cidadeUsuario'] = resul['cidadeUsuario']
                request.session['distanciaFeed'] = resul['distanciaFeed']
                request.session['uidFirebase'] = resul['uidFirebase']
            else:
                raise Http404
        else:
            raise Http404

        return JsonResponse(resul, safe=False)

