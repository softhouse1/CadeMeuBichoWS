from django.http.response import JsonResponse

from cademeubicho.conexao import Conexao
import MySQLdb
import json

class UsuarioDao:


    def insertUsuario(request, param):
        cx = Conexao()
        cx.conectar()
        sql = """ insert into Usuarios (
                    nomeUsuario, 
                    numeroCelular,
                    dddCelular,
                    distanciaFeed ,
                    emailUsuario ,
                    idFacebook ,
                    uidFirebase,
            ) values (
                %(nomeUsuario)s,
                %(numeroCelular)s,
                %(dddCelular)s,
                CAST_TO_INTEGER (%(distanciaFeed)s ),
                %(emailUsuario)s,
                %(idFacebook)s,
                %(UidFirebase)s ) """
        rows = ''
        try:
            rows = cx.executa(sql, param, True)
        except BaseException as e:
            print (e)
            rows = {'RowsEffect': "0"}

        return rows

    def update_usuario(request, param):
        cx = Conexao()
        cx.conectar()

        sql = """ update Usuarios set
                    nomeUsuario = %(nomeUsuario)s,
                    numeroCelular = %(numeroCelular)s,
                    dddCelular = %(dddCelular)s,
                    distanciaFeed = CAST_TO_INTEGER (%(distanciaFeed)s ),
                    emailUsuario =  %(emailUsuario)s                WHERE  uidFirebase = %(UidFirebase)s """

        rows = ''
        try:
            rows = cx.executa(sql, param, True)
        except BaseException:
            rows = {'RowsEffect': "0"}

        return rows
