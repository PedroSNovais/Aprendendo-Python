from uteis115 import *
print(f'{" Desafio 115 ":*^40}')
while True:
    titulo()
    print('\033[33m 1 - \033[36mVer pessoas cadastradas \n \033[33m2 - \033[36mCadastrar nova pessoa \n \033[33m3 - '
          '\033[36mSair do programa\033[m')
    r = continuar()
    if r == 1:
        titulo("PESSOAS CADASTRADAS")
        arq = open('arquivo.txt', 'r')
        print(arq.read())
        arq.close()
    elif r == 3:
        break
    elif r == 2:
        p = dados()
        dado = f'{p["nome"]:<31} {p["idade"]} anos\n'
        arq = open('arquivo.txt', 'a')
        arq.writelines(dado)
        print('\033[1;32mPessoa cadastrada com sucesso !!\033[m')
        arq.close()
print('<<<<< Fim do Programa >>>>')
