from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Repositories import PostAnimalDao


class PostAnimal:

    @csrf_exempt
    def cadastra_post_animal(request):
        retorno = ''
        if request.POST:
            post = PostAnimalDao()
            paramAnimais = {
                    'uidFirebase': request.POST.get('uidFirebase'),
                    'porteAnimal': request.POST.get('porteAnimal'),
                    'tipoAnimal': request.POST.get('tipoAnimal'),
                    'nomeAnimal': request.POST.get('nomeAnimal'),
                    'racaAnimal': request.POST.get('racaAnimal'),
                    'idadeAnimal': request.POST.get('idadeAnimal'),
                    'corAnimal': request.POST.get('corAnimal'),
                    'recompensa': request.POST.get('recompensa'),
                    'longitude': request.POST.get('longitude'),
                    'latitude': request.POST.get('latitude')
                     }
            imagens = { 'imagens' : request.POST.get('imagens') }

            print(paramAnimais)
            postAtivos = post.posts_ativo_usuario( paramAnimais )

            if paramAnimais['uidFirebase'] == '' or paramAnimais['uidFirebase'] == None:
                retorno = {'statusMensagem': 'Usuário não autenticado', 'retorno': 'false'}
            elif postAtivos[0]['qnt'] != 0:
                retorno = { 'statusMensagem' : 'Usuário já possui um Post ativo', 'retorno' : 'false'}
            elif len(imagens) <= 0:
                retorno = {'statusMensagem': 'Escolha ao menos uma imagem', 'retorno': 'false'}
            else :
                rows = post.insere_post(paramAnimais)
                if rows['RowsEffect'] != "0":
                    idAnimal = post.getIdPostAtivo(paramAnimais)[0]['CODIGO']
                    imagens.update({'idAnimal' : idAnimal})

                    fotosInseridas = post.insere_imagem_post(imagens)

                    if fotosInseridas > 0:
                        retorno =  { 'statusMensagem': 'Post cadastrado com sucesso', 'retorno' : 'true'}
                    else:
                        retorno =  { 'statusMensagem': 'Erro ao inserir imagens', 'retorno' : 'false'}

                else:
                    retorno = { 'statusMensagem' : 'Erro ao cadastrar post', 'retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)

    @csrf_exempt
    def atualiza_post_animal(request):
        retorno = ''
        post = PostAnimalDao()
        if request.POST:
            paramAnimais = {
                    'uidFirebase': request.POST.get('uidFirebase'),
                    'porteAnimal': request.POST.get('porteAnimal'),
                    'tipoAnimal': request.POST.get('tipoAnimal'),
                    'nomeAnimal': request.POST.get('nomeAnimal'),
                    'racaAnimal': request.POST.get('racaAnimal'),
                    'idadeAnimal': request.POST.get('idadeAnimal'),
                    'corAnimal': request.POST.get('corAnimal'),
                    'recompensa': request.POST.get('recompensa'),
                    'longitude': request.POST.get('longitude'),
                    'latitude': request.POST.get('latitude')
            }
            imagens = {'imagens': request.POST.get('imagens')}

            if paramAnimais['uidFirebase'] == '':
                retorno = {'statusMensagem': 'Usuário não autenticado', 'retorno': 'false'}

            elif len(imagens) <= 0:
                retorno = {'statusMensagem': 'Escolha ao menos uma imagem', 'retorno': 'false'}

            #PRONTO PARA EDICAO
            else:
                rows = post.atualiza_post(paramAnimais)
                if int(rows['RowsEffect'] ) >= 0:

                    print("IMAGENS", imagens)
                    if  imagens['imagens'] != 'NAO_ALTERAR_IMAGEM':
                        idAnimal = post.getIdPostAtivo(paramAnimais)[0]['CODIGO']
                        imagens.update({'idAnimal': idAnimal})
                        post.removeFotosPost(paramAnimais)
                        fotosInseridas = post.insere_imagem_post(imagens)
                    else :
                        fotosInseridas = 1

                    if fotosInseridas > 0:
                        retorno = {'statusMensagem': 'Post atualizado com sucesso', 'retorno': 'true'}
                    else:
                        retorno = {'statusMensagem': 'Erro ao inserir imagens', 'retorno': 'false'}

                else:
                    retorno = {'statusMensagem': 'Post não atualizado!', 'retorno': 'false'}

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
            if rows['RowsEffect'] != "0":
               retorno =  { 'statusMensagem': 'Post desativado com sucesso', 'retorno' : 'true'}
            else:
                retorno = { 'statusMensagem' : 'Erro ao desativar post', 'retorno' : 'false'}
        else:
            raise Http404

        return JsonResponse(retorno, safe=False)

    @csrf_exempt
    def get_posts_proximos(request):
        param = {
            'uidFirebase': request.POST.get('uidFirebase'),
            'longitudeAtual': request.POST.get('longitude'),
            'latitudeAtual': request.POST.get('latitude')
        }
        post = PostAnimalDao()
        resul = []
        resul = post.get_post(param, False)

        # if resul == []:
        #     resul = [{'statusMensagem': 'Nenhum post Localizado', 'retorno': 'false'}]
        return JsonResponse({'Posts': resul})

    @csrf_exempt
    def get_posts_usuario(request):
        param = {
            'uidFirebase' : request.POST.get('uidFirebase') ,
            'longitudeAtual': request.POST.get('longitude'),
            'latitudeAtual' : request.POST.get('latitude')
        }
        post = PostAnimalDao()
        resul = []
        resul = post.get_post(param, True)

        # if resul == [] :
            # resul = [{'statusMensagem' : 'Nenhum post Localizado', 'retorno' : 'false'}]
        return JsonResponse({'Posts': resul})


