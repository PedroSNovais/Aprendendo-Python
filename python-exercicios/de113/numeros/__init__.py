def leiaint(__prompt__='Digite um numero inteiro: '):
    while True:
        try:
            n = int(input(__prompt__).strip())
            return n
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO com os dados digitados.\033[m')
        except Exception as error:
            print(f'ERRO! tipo do erro: {error.__cause__}')


def leiafloat(__prompt__='Digite um numero real: '):
    while True:
        try:
            n = str(input(__prompt__).strip())
            if n in ',':
                n.replace(',', '.')
            return float(n)
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO com os dados digitados.\033[m')
        except Exception as error:
            print(f'ERRO! tipo do erro: {error.__cause__}')
