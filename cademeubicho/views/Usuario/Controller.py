from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Repositories import UsuarioDao
from cademeubicho.views.Login.Repositories import LoginDao


class Usuario:

    @csrf_exempt
    def cadastra_usuario(request):
        retorno = ''
        if request.POST:
            ld = LoginDao()
            print(request)
            print(request.POST)
            param = {
                    'UidFirebase': request.POST.get('uidFirebase'),
                    'nomeUsuario': request.POST.get('nomeUsuario'),
                    'distanciaFeed': request.POST.get('distanciaFeed'),
                    'emailUsuario': request.POST.get('emailUsuario'),
                    'numeroCelular': request.POST.get('numeroCelular'),
                    'dddCelular': request.POST.get('dddCelular')
                     }

            resul = ld.get_usuario( param )
            if resul != []:
                retorno = { 'StatusMensagem' : 'Usuário já cadastrado', 'Retorno' : 'false'}
            else:
                userDao = UsuarioDao()
                rows = userDao.insertUsuario(param)
                print (rows)
                if rows['RowsEffect'] != "0":
                   retorno =  { 'StatusMensagem': 'Usuário cadastrado com sucesso', 'Retorno' : 'true'}
                else:
                    retorno = { 'StatusMensagem' : 'Erro ao cadastrar Usúario', 'Retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)


    @csrf_exempt
    def atualiza_usuario(request):
        retorno = ''
        print(request)
        print(request.POST)
        if request.POST:
            ld = LoginDao()
            param = {
                    'UidFirebase': request.POST.get('uidFirebase'),
                    'nomeUsuario': request.POST.get('nomeUsuario'),
                    'distanciaFeed': request.POST.get('distanciaFeed'),
                    'emailUsuario': request.POST.get('emailUsuario'),
                    'numeroCelular': request.POST.get('numeroCelular'),
                    'dddCelular': request.POST.get('dddCelular')
                     }

            userDao = UsuarioDao()
            rows = userDao.update_usuario(param)
            print (rows)
            if rows['RowsEffect'] != "0":
               retorno =  { 'StatusMensagem': 'Usuário atualizado com sucesso', 'Retorno' : 'true'}
            else:
                retorno = { 'StatusMensagem' : 'Erro ao atualizar Usúario', 'Retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)
