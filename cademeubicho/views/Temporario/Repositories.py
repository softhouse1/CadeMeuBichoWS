from cademeubicho.conexao import Conexao
import MySQLdb
import json

class TempDao:

    def busca_usuarios(self):
        cx = Conexao()
        cx.conectar()

        sql = """select * from Usuarios"""
        tipo = cx.select(sql)
        return tipo

    def busca_posts(self):
        cx = Conexao()
        cx.conectar()

        sql = """select * from Animais"""
        tipo = cx.select(sql)
        return tipo


    def busca_posts_completo(self):
        cx = Conexao()
        cx.conectar()
        sql = """SELECT 
            POST.nomeAnimal, 
            TIPO.descricaoTipo ,
            PORTE.descricaoPorte ,
            POST.racaAnimal,
            POST.corAnimal,
            POST.recompensa ,
            POST.permiteContato ,
            POST.longitude ,
            POST.latitude ,
            POST.cadastroAtivo AS postAtivo,
            POST.horaCadastro,
            USU.nomeUsuario ,
            USU.dddCelular ,
            USU.numeroCelular ,
            ( round (ST_Distance_Sphere(
                point(POST.longitude , POST.latitude ),
                point( '0', '0' )
                ) / 1000 ,3.2 ) <=
                ( SELECT usu_logado.distanciaFeed 
                FROM Usuarios usu_logado
                WHERE usu_logado.uidFirebase = '0'
            ) ) AS distanciaKM
        FROM Animais POST
            INNER JOIN PorteAnimal PORTE
                ON PORTE.idPorte = POST.idPorte 
            INNER JOIN Cade_meu_bicho.TipoAnimal TIPO
                ON TIPO.idTipo = POST.idTipo
            INNER JOIN Usuarios USU
                ON USU.idUsuario = POST.idDono
        """
        tipo = cx.select(sql)
        return tipo
