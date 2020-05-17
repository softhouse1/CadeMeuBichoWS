from ...conexao import *
import requests
import json

class FuncoesDao:

    def realiza_filtro(self, dados, chave_dados, valor_procurado):
        lista = []
        for i in dados:
            if i[chave_dados] == valor_procurado:
                lista.append(i)
        return lista