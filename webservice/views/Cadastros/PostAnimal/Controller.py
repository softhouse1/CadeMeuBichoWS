from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Repositories import PostAnimalDao


class PostAnimal:

    @csrf_exempt
    def cadastra_post_animal(request):
        retorno = ''
        if request.POST:
            post = PostAnimalDao()
            param = {
                    'uidFirebase': request.POST.get('uidFirebase'),
                    'porteAnimal': request.POST.get('porteAnimal'),
                    'tipoAnimal': request.POST.get('tipoAnimal'),
                    'nomeAnimal': request.POST.get('nomeAnimal'),
                    'racaAnimal': request.POST.get('racaAnimal'),
                    'idadeAnimal': request.POST.get('idadeAnimal'),
                    'corAnimal': request.POST.get('corAnimal'),
                    'recompensa': request.POST.get('recompensa'),
                    'permiteContato': request.POST.get('permiteContato'),
                    'logitude': request.POST.get('logitude'),
                    'latitude': request.POST.get('latitude')
                     }

            postAtivos = post.posts_ativo_usuario( param )
            if postAtivos != "0":
                retorno = { 'StatusMensagem' : 'Usuário já possui um Post ativo', 'Retorno' : 'false'}
            else:
                rows = post.insere_post(param)
                if rows['RowsEffect'] != "0":
                   retorno =  { 'StatusMensagem': 'Post cadastrado com sucesso', 'Retorno' : 'true'}
                else:
                    retorno = { 'StatusMensagem' : 'Erro ao cadastrar post', 'Retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)

    @csrf_exempt
    def atualiza_post_animal(request):
        retorno = ''
        if request.POST:
            param = {
                    'uidFirebase': request.POST.get('uidFirebase'),
                    'porteAnimal': request.POST.get('porteAnimal'),
                    'tipoAnimal': request.POST.get('tipoAnimal'),
                    'nomeAnimal': request.POST.get('nomeAnimal'),
                    'racaAnimal': request.POST.get('racaAnimal'),
                    'idadeAnimal': request.POST.get('idadeAnimal'),
                    'corAnimal': request.POST.get('corAnimal'),
                    'recompensa': request.POST.get('recompensa'),
                    'permiteContato': request.POST.get('permiteContato'),
                    'logitude': request.POST.get('logitude'),
                    'latitude': request.POST.get('latitude')
                     }

            posts = PostAnimalDao()
            rows = posts.atualiza_post(param)
            print (rows)
            if rows['RowsEffect'] != "0":
               retorno =  { 'StatusMensagem': 'Post atualizado com sucesso', 'Retorno' : 'true'}
            else:
                retorno = { 'StatusMensagem' : 'Erro ao atualizar post', 'Retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)

    @csrf_exempt
    def desativa_post(request):
        retorno = ''
        if request.POST:
            param = { 'uidFirebase': request.POST.get('uidFirebase') }

            posts = PostAnimalDao()
            rows = posts.desativa_post(param)
            print (rows)
            if rows['RowsEffect'] != "0":
               retorno =  { 'StatusMensagem': 'Post desativado com sucesso', 'Retorno' : 'true'}
            else:
                retorno = { 'StatusMensagem' : 'Erro ao desativar post', 'Retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)

    @csrf_exempt
    def get_posts_proximos(request):
        param = {
            'uidFirebase': request.POST.get('uidFirebase'),
            'longitudeAtual': request.POST.get('longitudeAtual'),
            'latitudeAtual': request.POST.get('latitudeAtual')
        }
        post = PostAnimalDao()
        resul = []
        resul = post.get_post(param, False)

        if resul == []:
            resul = [{'StatusMensagem': 'Nenhum post Localizado', 'Retorno': 'false'}]
        return JsonResponse({'Posts': resul})

    @csrf_exempt
    def get_posts_usuario(request):
        param = {
            'uidFirebase' : request.POST.get('uidFirebase') ,
            'longitudeAtual': request.POST.get('longitudeAtual'),
            'latitudeAtual' : request.POST.get('latitudeAtual')
        }
        post = PostAnimalDao()
        resul = []
        resul = post.get_post(param, True)

        if resul == [] :
            resul = [{'StatusMensagem' : 'Nenhum post Localizado', 'Retorno' : 'false'}]
        return JsonResponse({'Posts': resul})
