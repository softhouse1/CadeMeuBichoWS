from django.http.response import JsonResponse

from CadeMeuBicho.webservice.conexao import Conexao
import MySQLdb
import json

class LoginDao:


    def get_usuario(request, param):
        cx = Conexao()
        cx.conectar()
        sql = """ select 
                    nomeUsuario, 
                    numeroCelular, 
                    dddCelular, 
                    emailUsuario,
                    ufUsuario,
                    cidadeUsuario ,
                    distanciaFeed,
                    uidFirebase
                from Cade_meu_bicho.Usuarios u 
                where upper(cadastroAtivo) = 'S'
                and uidFirebase =  %(UidFirebase)s 
                """
        user = []
        user = cx.select(sql, param)

        return user

