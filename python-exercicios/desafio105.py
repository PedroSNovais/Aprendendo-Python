from teste import titulo


def notas(*n, sit=False):
    """
     -> le notas de alunos e fornece dados
    :param n: uma ou mais notas (pode receber varias)
    :param sit: (opcional) se True mostra a situação
    :return: um dicionario com os dados do aluno
    """
    dados = dict()
    dados["media"] = 0
    cont = 0
    for nota in n:
        if cont == 0:
            dados["maior"] = dados["menor"] = nota
        elif nota > dados["maior"]:
            dados["maior"] = nota
        elif nota < dados["menor"]:
            dados["menor"] = nota
        dados["media"] += nota
        cont += 1
    dados["media"] = dados["media"] / 2
    if sit:
        if dados["media"] > 7:
            dados["situação"] = 'Boa'
        elif 5 < dados["media"] < 7:
            dados["situação"] = 'Razoavel'
        else:
            dados["situação"] = 'Ruim'
    dados["media"] /= 2
    dados["contidade de notas lidas"] = cont
    return dados


# programa principal
titulo('Desafio 105')
aluno = notas(8, 6.5, 1)
for k, v in aluno.items():
    print(f' -> {k} é igual a {v}.')
help(notas)
