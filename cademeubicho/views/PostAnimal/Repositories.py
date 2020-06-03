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
                0.00,
                trim( %(longitude)s  ),
                trim( %(latitude)s  )
            FROM Usuarios u 
            WHERE u.uidFirebase  = %(uidFirebase)s
            and u.cadastroAtivo = 'S'
            LIMIT 1  """
        rows = ''
        try:
            rows = cx.executa(sql, param, True)
        except BaseException:
            rows = {'RowsEffect': "0"}

        return rows

    def atualiza_post(request, param):
        cx = Conexao()
        cx.conectar()
        sql = """ update Animais set  
                    idPorte = get_id_porte (  %(porteAnimal)s ),
                    idTipo = get_id_tipo_animal (  %(tipoAnimal)s ),
                    nomeAnimal = upper(trim( %(nomeAnimal)s  )),
                    racaAnimal = upper(trim( %(racaAnimal)s  )),
                    idadeAprox = CAST_TO_INTEGER (%(idadeAnimal)s ),
                    corAnimal = upper(trim( %(corAnimal)s  )),
                    recompensa = 0.00,
                    longitude = trim( %(longitude)s  ),
                    latitude = trim( %(latitude)s  )
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
            # OBS - CASO NÃO TIVER UID NA REQUISICAO
            # (EX. USUARIO VISITANTE - IRA MOSTRAR POST ATÉ 35 KM)
            clausura = """ AND POST.cadastroAtivo = 'S'
                            AND round (ST_Distance_Sphere(
                                point(POST.longitude , POST.latitude ),
                                point(%(longitudeAtual)s , %(latitudeAtual)s )
                            ) / 1000 ,3 ) <= 
                                COALESCE (( SELECT usu_logado.distanciaFeed
                                    FROM Usuarios usu_logado
                                    WHERE usu_logado.uidFirebase = %(uidFirebase)s
                                ),35) """


        sql = """SELECT 
                POST.nomeAnimal, 
                TIPO.descricaoTipo ,
                PORTE.descricaoPorte ,
                POST.racaAnimal,
                POST.corAnimal,
                POST.recompensa ,
                POST.longitude ,
                POST.latitude ,
                POST.cadastroAtivo AS postAtivo,
                POST.horaCadastro,
                USU.nomeUsuario ,
                USU.dddCelular ,
                USU.numeroCelular ,
                USU.ufUsuario ,
                USU.cidadeUsuario,
                ( round (ST_Distance_Sphere(
                    point(POST.longitude , POST.latitude ),
                    point( %(longitudeAtual)s, %(latitudeAtual)s )
                    ) / 1000 ,3.2 ) <=
                    ( SELECT usu_logado.distanciaFeed 
                    FROM Usuarios usu_logado
                    WHERE usu_logado.uidFirebase = %(uidFirebase)s
                ) ) AS distanciaKM
            FROM Animais POST
                INNER JOIN PorteAnimal PORTE
                    ON PORTE.idPorte = POST.idPorte 
                INNER JOIN TipoAnimal TIPO
                    ON TIPO.idTipo = POST.idTipo
                INNER JOIN Usuarios USU
                    ON USU.idUsuario = POST.idDono
            WHERE 
                USU.cadastroAtivo = 'S'"""

        sql += clausura + "order by 17 ASC , POST.horaCadastro desc"


        posts = cx.select(sql, param)

        print(posts)
        for i in posts:
            i['imagens'] = ["", "", ""]


        return posts