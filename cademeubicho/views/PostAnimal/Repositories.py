from cademeubicho.conexao import Conexao

class PostAnimalDao:


    def insere_post(request, param):
        cx = Conexao()
        cx.conectar()

        sql = """ insert into Animais ( 
                idDono,
                idPorte,
                idTipo,
                nomeAnimal,
                racaAnimal,
                idadeAprox,
                corAnimal,
                recompensa,
                longitude,
                latitude
            ) SELECT 
                u.idUsuario,
                get_id_porte (  %(porteAnimal)s ),
                get_id_tipo_animal (  %(tipoAnimal)s ),
                upper(trim( %(nomeAnimal)s  ) ),
                upper(trim( %(racaAnimal)s  ) ),
                CAST_TO_INTEGER (%(idadeAnimal)s ),
                upper(trim( %(corAnimal)s  )),
                %(recompensa)s ,
                trim( %(longitude)s  ),
                trim( %(latitude)s  )
            FROM Usuarios u 
            WHERE u.uidFirebase  = %(uidFirebase)s
            and u.cadastroAtivo = 'S'
            LIMIT 1  """
        rows = ''
        try:
            param['recompensa'] = float(param['recompensa'])
            rows = cx.executa(sql, param, True)
        except BaseException:
            rows = {'RowsEffect': "0", "Error" : rows}

        return rows

    def atualiza_post(request, param):
        cx = Conexao()
        cx.conectar()
        sql = f""" Update Animais set  
                    idPorte = get_id_porte ( '{param['porteAnimal']}'  ),
                    idTipo = get_id_tipo_animal ( '{param['tipoAnimal']}'  ),
                    nomeAnimal = upper(trim( '{param['nomeAnimal']}'  )),
                    racaAnimal = upper(trim( '{param['racaAnimal']}'  )),
                    idadeAprox = CAST_TO_INTEGER ( {param['idadeAnimal']} ),
                    corAnimal = upper(trim( '{param['corAnimal']}' )),
                    recompensa = {param['recompensa']},
                    longitude = trim( '{param['longitude']}' ), latitude = trim( '{param['latitude']}' )
                where cadastroAtivo = 'S'
                and idDono  = 
                    (SELECT u.idUsuario FROM Usuarios u 
                        WHERE u.uidFirebase  = '{param['uidFirebase']}'
                        and u.cadastroAtivo = 'S'
                        LIMIT 1
                    ) """

        rows = ''
        try:
            param['recompensa'] = float(param['recompensa'])
            rows = cx.executa(sql, commit=True)
        except BaseException:
            raise
            rows = {'RowsEffect': -1}

        return rows

    def desativa_post(request, param):
        cx = Conexao()
        cx.conectar()

        sql = """ update Animais set  
                    cadastroAtivo = 'N'
                where cadastroAtivo = 'S'
                and idDono  = 
                    (SELECT u.idUsuario FROM Usuarios u 
                        WHERE u.uidFirebase  = %(uidFirebase)s
                        and u.cadastroAtivo = 'S'
                        LIMIT 1
                    ) """

        rows = ''
        try:
            rows = cx.executa(sql, param, True)
        except BaseException:
            rows = {'RowsEffect': "0"}

        return rows

    def posts_ativo_usuario (request, param):
        cx = Conexao()
        cx.conectar()

        uid = {'uidFirebase' : param['uidFirebase']}

        sql = """select coalesce( (select COUNT(1) from Animais
                where cadastroAtivo = 'S'
                and idDono  = 
                    (SELECT u.idUsuario FROM Usuarios u 
                        WHERE u.uidFirebase  = %(uidFirebase)s
                        and u.cadastroAtivo = 'S'
                        LIMIT 1
                    )
                 ),0) as qnt from dual"""

        return  cx.select(sql, param)


    def get_post (request, param, apenasPostUsuario=False):
        cx = Conexao()
        cx.conectar()
        clausura = ''


        if apenasPostUsuario :
            clausura = """ AND USU.uidFirebase = %(uidFirebase)s """
        else :
            pass
            # OBS - CASO NÃO TIVER UID NA REQUISICAO
            # (EX. USUARIO VISITANTE - IRA MOSTRAR POST ATÉ 35 KM)
            clausura = """ AND POST.cadastroAtivo = 'S' """
                            # AND COALESCE(round (ST_Distance(
                            #     point(POST.longitude , POST.latitude ),
                            #     point(%(longitudeAtual)s , %(latitudeAtual)s )
                            # ) / 1000 ,3 ),0) <=
                            #     COALESCE (( SELECT usu_logado.distanciaFeed
                            #         FROM Usuarios usu_logado
                            #         WHERE usu_logado.uidFirebase = %(uidFirebase)s
                            #     ),35) """


        sql = """ SELECT 
                USU.idUsuario as idUsuario,
                USU.uidFirebase as idFirebaseUsu,
                POST.idAnimal AS ID_POST,
                POST.nomeAnimal, 
                TIPO.descricaoTipo ,
                PORTE.descricaoPorte ,
                POST.racaAnimal,
                POST.corAnimal,
                POST.recompensa ,
                POST.longitude , 
                POST.latitude ,
                POST.idadeAprox as idadeAnimal,
                POST.cadastroAtivo AS postAtivo,
                cast(POST.horaCadastro as char) as horaCadastro,
                USU.nomeUsuario,
                case when USU.numeroCelular is null or USU.numeroCelular = '' then 
                    ''
                else
                CONCAT('https://api.whatsapp.com/send?phone=+55', USU.dddCelular, USU.numeroCelular)
                end as celularWhatsApp,
                USU.dddCelular, USU.numeroCelular,
                coalesce(USU.idFacebook,'') idFacebook,
                COALESCE(( round (ST_Distance(
                    point(POST.longitude , POST.latitude ),
                    point( %(longitudeAtual)s, %(latitudeAtual)s )
                    ) / 1000 ,3.2 ) <=
                    ( SELECT usu_logado.distanciaFeed 
                    FROM Usuarios usu_logado
                    WHERE usu_logado.uidFirebase = %(uidFirebase)s
                ) ),35) AS distanciaKM
            FROM Animais POST
                INNER JOIN PorteAnimal PORTE
                    ON PORTE.idPorte = POST.idPorte 
                INNER JOIN TipoAnimal TIPO
                    ON TIPO.idTipo = POST.idTipo
                INNER JOIN Usuarios USU
                    ON USU.idUsuario = POST.idDono
            WHERE 
                USU.cadastroAtivo = 'S' """

        sql += clausura + " order by distanciaKM ASC , POST.horaCadastro desc limit 3"

        posts = cx.select(sql, param)


        for p in posts:
            imagens = request.get_imagem_post(p['ID_POST'], cx)
            p['imagens'] =[]
            for  i in imagens:
                p['imagens'].append(i['imagem'])

            del p['ID_POST']

        return posts


    def getIdPostAtivo(self, param):
        cx = Conexao()
        cx.conectar()

        post = { 'uidFirebase' : param['uidFirebase'] }

        sql = """
            SELECT idAnimal as CODIGO
                FROM Animais POST
                INNER JOIN Usuarios USU
                    ON USU.idUsuario = POST.idDono
            WHERE 
                USU.cadastroAtivo = 'S'
                AND USU.uidFirebase  = %(uidFirebase)s
                AND POST.cadastroAtivo = 'S'
                LIMIT 1 """

        return cx.select(sql, post)


    def removeFotosPost(self, param):
        cx = Conexao()
        cx.conectar()
        p = {'uidFirebase' : param['uidFirebase']}
        sql = """ DELETE FROM FotosAnimal WHERE idAnimal in (
            SELECT a.idAnimal FROM Animais a
                inner join Usuarios u
                    on a.idDono = u.Usuario
                    AND u.uidFirebase  = %(uidFirebase)s 
                WHERE a.cadastroAtivo = 'S'
        )"""
        try:
            cx.executa(sql, p, True)
        except Exception :
            return False
        return True

    def insere_imagem_post(self, param):
        cx = Conexao()
        cx.conectar()
        fotosInseridas = 0

        for i in param['imagens'].split("***0ba)img&0@&e4**"):
            try:

                if i != '' and i != 'NAO_ALTERAR_IMAGEM':
                    sql = f"""INSERT INTO FotosAnimal (idAnimal	, imagem) VALUES (%(idAnimal)s, '{i}')"""
                    rows = cx.executa(sql, param, True)
                    fotosInseridas += 1
            except BaseException:
                fotosInseridas += 0

        return fotosInseridas


    def get_imagem_post(request, idPost, con):
        return con.select("SELECT imagem FROM FotosAnimal WHERE idAnimal = "+str(idPost))
