from django.http.response import JsonResponse

from cademeubicho.conexao import Conexao
import MySQLdb
import json

class UsuarioDao:


    def insertUsuario(request, param):
        cx = Conexao()
        cx.conectar()
        sql = """ insert into Cade_meu_bicho.Usuarios (
                    nomeUsuario, 
                    numeroCelular,
                    dddCelular,
                    ufUsuario,
                    cidadeUsuario ,
                    distanciaFeed ,
                    emailUsuario ,
                    uidFirebase
            ) values (
                %(nomeUsuario)s,
                %(numeroCelular)s,
                %(dddCelular)s,
                %(ufUsuario)s,
                %(cidadeUsuario)s,
                Cade_meu_bicho.CAST_TO_INTEGER (%(distanciaFeed)s ),
                %(emailUsuario)s,
                %(UidFirebase)s ) """
        rows = ''
        try:
            rows = cx.executa(sql, param, True)
        except BaseException:
            rows = {'RowsEffect': "0"}

        return rows

    def update_usuario(request, param):
        cx = Conexao()
        cx.conectar()

        sql = """ update Cade_meu_bicho.Usuarios set
                    nomeUsuario = %(nomeUsuario)s,
                    numeroCelular = %(numeroCelular)s,
                    dddCelular = %(dddCelular)s,
                    ufUsuario = %(ufUsuario)s,
                    cidadeUsuario = %(cidadeUsuario)s,
                    distanciaFeed = Cade_meu_bicho.CAST_TO_INTEGER (%(distanciaFeed)s ),
                    emailUsuario =  %(emailUsuario)s                WHERE  uidFirebase = %(UidFirebase)s """

        rows = ''
        try:
            rows = cx.executa(sql, param, True)
        except BaseException:
            rows = {'RowsEffect': "0"}

        return rows
