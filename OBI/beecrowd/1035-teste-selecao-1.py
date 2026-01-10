def teste_selecao(lista: list) -> str:
    if lista[0] % 2 != 0:
        return "Valores não aceitos"
    if lista[1] < lista[2]:
        return "Valores não aceitos"
    if lista[3] < lista[0]:
        return "Valores não aceitos"
    if (lista[2] + lista[3]) < (lista[0] + lista[1]):
        return "Valores não aceitos"
    if lista[2] < 0 and lista[3] < 0:
        return "Valores não aceitos"
    return "Valores aceitos"

n = map(int, input().split())
print(teste_selecao(list(n)))