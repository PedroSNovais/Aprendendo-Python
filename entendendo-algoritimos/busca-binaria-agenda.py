def busca_binaria_agenda(agenda: list, alvo: str) -> int:
    """
    Busca por um nome específico numa agenda

    param: 
        agenda: list -> Lista de strings em ordem alfabetica 
        alvo: string -> String que será buscada na lista
    return: 
        O indice da String desejada ou -1 se não existir na lista
    """
    baixo = 0
    alto = len(agenda) - 1

    while baixo <= alto:
        chute = (baixo + alto) // 2
        if agenda[chute] == alvo:
            return chute
        elif agenda[chute] > alvo:
            alto = chute - 1
        else:
            baixo = chute + 1
    return -1

# Testando

nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Isabela", "João", "Lucas", "Mariana", "Natália", "Otávio", "Paula"]
print(busca_binaria_agenda(nomes, "Gabriel"))
print(busca_binaria_agenda(nomes, "Pedro"))