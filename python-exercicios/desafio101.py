from teste import titulo


def voto(nasc):
    """
     -> ve se a pessoa tem que votar
    :param nasc: ano de nascimento
    :return: se o voto é 'OBRIGATORIO', 'OPCIONAL' ou ' Negado'
    """
    from datetime import date
    hj = date.today().year
    idade = hj - nasc

    if idade >= 65 or idade in (16, 17):
        return f'Para uma pessoa de {idade} anos, o Voto é Opicional!'
    elif idade >= 18:
        return f'Para uma pessoa de {idade} anos, o Voto é Obrigatorio!'
    else:
        return f'Para uma pessoa de {idade} anos, o Voto é Negado!'


titulo('Desafio 101')
resp = voto(int(input('Ano de nascimento: ')))
print(resp)
