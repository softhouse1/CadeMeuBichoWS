from cademeubicho.conexao import Conexao

class PorteAnimalDao:

    def busca_porte(self):
        cx = Conexao()
        cx.conectar()

        sql = """select descricaoPorte from cademeubicho.PorteAnimal"""
        tipo = cx.select(sql)
        return tipo

