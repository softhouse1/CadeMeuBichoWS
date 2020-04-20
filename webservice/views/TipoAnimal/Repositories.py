from CadeMeuBicho.webservice.conexao import Conexao
import MySQLdb
import json

class TipoAnimalDao:

    def busca_tipos(self):
        cx = Conexao()
        cx.conectar()

        sql = """select descricaoTipo from Cade_meu_bicho.TipoAnimal"""
        tipo = cx.select(sql)
        return tipo