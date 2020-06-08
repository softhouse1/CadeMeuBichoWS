from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Repositories import UsuarioDao
from cademeubicho.views.Login.Repositories import LoginDao


def retorna_telefone(ddd, telefone):
    try:
        ddd = str(int(ddd))
        telefone = str(int(telefone))
    except:
        return '', ''

    if ddd not in ('11', '12', '13', '14', '15', '16', '17', '18',
                   '19', '21', '22', '24', '27', '28', '31', '32',
                   '33', '34', '35', '37', '38', '41', '42', '43',
                   '44', '45', '46', '47', '48', '49', '51', '53',
                   '54', '55', '61', '62', '63', '64', '65', '66',
                   '67', '68', '69', '71', '73', '74', '75', '77',
                   '79', '81', '82', '83', '84', '85', '86', '87',
                   '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99'):
        return {'Erro': 'Erro', 'Mensagem': 'DDD Inválido'}
    elif len(telefone) < 8 or len(telefone) > 9:
        return {'Erro': 'Erro', 'Mensagem': 'Telefone com tamanho inválido'}

    elif (len(telefone) == 9 and int(telefone[0]) < 5) or (len(telefone) == 8 and int(telefone[0]) < 2):
        return {'Erro': 'Erro', 'Mensagem': 'Número de telefone inválido!'}


    elif len(telefone) == 8 and int(telefone[0]) >= 5:
        telefone = "9" + telefone

    return ddd, telefone


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
                retorno = { 'statusMensagem' : 'Usuário já cadastrado', 'retorno' : 'false'}
            else:

                userDao = UsuarioDao()
                rows = userDao.insertUsuario(param)
                print (rows)
                if rows['RowsEffect'] != "0":
                   retorno =  { 'statusMensagem': 'Usuário cadastrado com sucesso', 'retorno' : 'true'}
                else:
                    retorno = { 'statusMensagem' : 'Erro ao cadastrar Usúario', 'retorno' : 'false'}
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

            ret = retorna_telefone(param['dddCelular'], param['numeroCelular'])
            if 'Erro' in ret:
                return JsonResponse({'statusMensagem': ret['Mensagem'], 'retorno': 'false'}, safe=False)

            else:
                param['dddCelular'], param['numeroCelular'] = ret

            userDao = UsuarioDao()
            rows = userDao.update_usuario(param)
            print (rows)
            if rows['RowsEffect'] != "0":
               retorno =  { 'statusMensagem': 'Usuário atualizado com sucesso', 'retorno' : 'true'}
            else:
                retorno = { 'statusMensagem' : 'Erro ao atualizar Usúario', 'retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)

