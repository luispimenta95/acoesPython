import requests as req
import pandas as pd
import locale
import os
from dotenv import load_dotenv

load_dotenv()

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

nomes = pd.read_excel(os.getenv('path_dados'))
host = os.getenv('host')
pais = os.getenv('pais')

def busca_diaria():
    paises = []
    codes = []

    for nome in nomes['Codigo']:
        paises.append(nome + pais)
        codes.append(nome + '-' + pais)
    my_string = ','.join(codes)
    api_url = host+"last/" + my_string
    request = req.get(api_url)
    dados = request.json()
    if request.status_code == 200:
        print(f'Segue a ultima cotação das moedas pesquisadas: ')
        for nome in paises:
            print(f'{dados[nome]['name'] + ': ' + dados[nome]['high']}')

    else:
        print(dados['message'])

busca_diaria()
