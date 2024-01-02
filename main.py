from turtle import clear

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

def main():
    options = ['Busca diária', 'Busca por intervalo de dias']
    # Display options to the user
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    # Get user input
    selected_index = input("Escolha um numero de acordo com o módulo desejado para a pesquisa: ")
    # Validate user input
    try:
        selected_index = int(selected_index)
        if 1 <= selected_index <= len(options):
            if selected_index == 1:
                busca_diaria()
            elif selected_index == 2:
                busca_personalizada()
        else:
            print("Invalid input. Please enter a valid option number.")
    except ValueError:
        print("Invalid input. Please enter a number.")





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
def busca_personalizada():
    options = ['Euro', 'Dólar Americano', 'Bitcoin', 'Ethereum','Dolár Canadense' ]
    # Display options to the user
    print("Segue as moedas disponíveis para pesquisa:")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    # Get user input
    selected_index = input("Escolha um numero de acordo com a moeda desejada para a pesquisa: ")

    # Validate user input
    try:
        selected_index = int(selected_index)
        if 1 <= selected_index <= len(options):
            selected_option = options[selected_index - 1]
        else:
            print("Invalid input. Please enter a valid option number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


    codes = []

    for nome in nomes['Codigo']:
        codes.append(nome + '-' + pais)

    coin_code = codes[selected_index-1]
    intervalo = input("Informe um numero de dias para pesquisar a variaçao da moeda "  +selected_option +" : ")
    api_url = host + "json/daily/" + coin_code + "/" + intervalo
    request = req.get(api_url)
    dados = request.json()
    if request.status_code == 200:
        print(f'Seguem a(s) ultima(s) ' + intervalo + ' cotação(ões) do '+ selected_option +' : ')
        print(dados)
    else:
        print(dados['message'])




if __name__ == "__main__":
    main()
