from time import sleep


def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    sleep(0.7)
    mai = 0
    for n in num:
        if n > mai:
            mai = n
        print(n, end=' ')
        sleep(0.45)
    print(f'Foram digitados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


print(f'{" Desafio 99 ":-^40}')
maior(8, 9, 3, 4, 4, 5, 7, 2)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
