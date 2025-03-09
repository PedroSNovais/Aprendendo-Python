print(f'{"Desafio 43":=^30}')
peso = float(input('Qual o seu peso? KG '))
altura = float(input('qual a sua altura? Cm '))
imc = peso  / (altura / 100)**2
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print(f'\033[4;33mABAIXO DO PESO!\033[m')
elif imc < 25:
    print(f'\033[32mPESO IDEAL !\033[m')
elif imc < 30:
    print(f'\033[4;33mSOBREPESO!\033[m')
elif imc < 40:
    print(f'\033[4;31mOBESIDADE!\033[m')
elif imc > 40:
    print(f'\033[1;30;41mOBESIDADE MORBIDA !!!\033[m')
