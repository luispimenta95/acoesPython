import requests as req
import pandas as pd
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

nomes = pd.read_excel('teste.xlsx')
pais = 'BRL'
host = "https://economia.awesomeapi.com.br/"

def busca_diaria():
    paises = []
    codes = []

    for nome in nomes['Codigo']:
        paises.append(nome + pais)
        codes.append(nome + '-' + pais)
    my_string = ','.join(codes)
    api_url = host+"last/" + my_string
    request = req.get(api_url)
    if request.status_code == 200:
        dados = request.json()
        print(f'Segue a ultima cotação das moedas pesquisadas: ')
    for nome in paises:
        print(f'{dados[nome]['name'] + ': ' + dados[nome]['high']}')


busca_diaria()
