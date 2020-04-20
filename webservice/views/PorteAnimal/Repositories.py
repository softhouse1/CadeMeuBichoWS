from CadeMeuBicho.webservice.conexao import Conexao

class PorteAnimalDao:

    def busca_porte(self):
        cx = Conexao()
        cx.conectar()

        sql = """select descricaoPorte from Cade_meu_bicho.PorteAnimal"""
        tipo = cx.select(sql)
        return tipo

