from urllib.request import Request

from requests import get
print(f'{"Desafio 114":*^40}')
try:
    acesso = get('https://www.pudim.com.br/').status_code
    if acesso == 200:
        print('\033[1;32mO site do pudim está acessivel !\033[m')
    else:
        print('\033[1;31mO site do pudim não está acessivel!!\033[m')
except ConnectionError:
    print('\033[1;31mO site do pudim não está acessivel!!\033[m')
except Exception as error:
    print(error.__class__)