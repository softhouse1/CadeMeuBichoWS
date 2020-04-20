from ....conexao import Conexao

class PorteAnimalDao:

    def busca_porte(self):
        cx = Conexao()
        cx.conectar()

        sql = """select descricaoTipo from Cade_meu_bicho.TipoAnimal"""
        tipo = cx.select(sql)
        return tipo

