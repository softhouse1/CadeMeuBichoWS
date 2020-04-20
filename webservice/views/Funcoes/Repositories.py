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



    def consulta_estados_ibge(self, uf):
        header = {"Content-type": "application/json"}
        response = requests.request('GET', 'https://servicodados.ibge.gov.br/api/v1/localidades/estados',headers=header)
        estados = []

        if uf is None:
            for i in response.json():
                estados.append (i['sigla'])
        else:
            for i in response.json():
                if i['sigla'].upper() == uf.upper():
                    return i['id']
        return estados

    def consulta_cidades_ibge(self, estado):
        headers = {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'User-Agent': 'CADE-MEU-BICHO',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Connection': 'keep-alive',
                }
        id_estado = self.consulta_estados_ibge (estado)
        print (id_estado)
        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/'+str(id_estado)+'/municipios', headers=headers)
        cidades = []
        for i in response.json():
            cidades.append(i['nome'])
        return cidades