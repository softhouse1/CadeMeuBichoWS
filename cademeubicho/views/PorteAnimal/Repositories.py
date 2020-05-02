from cademeubicho.conexao import Conexao

class PorteAnimalDao:

    def busca_porte(self):
        cx = Conexao()
        cx.conectar()

        sql = """select descricaoPorte from PorteAnimal"""
        tipo = cx.select(sql)
        return tipo

