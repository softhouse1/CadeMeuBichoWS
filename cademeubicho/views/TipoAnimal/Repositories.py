from cademeubicho.conexao import Conexao
import MySQLdb
import json

class TipoAnimalDao:

    def busca_tipos(self):
        cx = Conexao()
        cx.conectar()

        sql = """select descricaoTipo from TipoAnimal"""
        tipo = cx.select(sql)
        return tipo