#funcão sem parametro
def linha():
    print('-' * 30)


# função com parametro
def soma(a, b):
    print(f'A = {a} \nB = {b}')
    s = a + b
    print(f'A soma de A + B é igual a = {s}')


# desempacotamento
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} numeros')


# usando listas
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# Programa principal
linha()
print('Aula 20')
linha()

soma(b=9, a=6)
soma(4, 8)
linha()

contador(2, 5, 6, 9)
contador(6, 9, 5, 8, 9, )
linha()

valores = [9, 8, 5, 6, 1]
print(valores)
dobra(valores)
print(valores)
