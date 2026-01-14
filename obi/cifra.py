# nivel2-2021-fase1

alfa = "a b c d e f g h i j k l m n o p q r s t u v x z".split()
vogais = "a e i o u ".split()

dist_vogais = []

p = str(input())
nova_p = ''

menor_dist = 90
vogal_proxima = 'z'

for letra in p:
    if letra in vogais:
        nova_p += letra
    else:
        menor_dist = 90
        vogal_proxima = 'z'
        dist_vogais = []
        
        nova_p += letra
        idx_consoante = alfa.index(letra)

        for vogal in vogais:
            idx_vogal = alfa.index(vogal)
            distancia = abs(idx_consoante - idx_vogal)
            dist_vogais.append((distancia, vogal))

        for tupla in dist_vogais:
            if tupla[0] == menor_dist:
                if alfa.index(tupla[1]) < alfa.index(vogal_proxima):
                    vogal_proxima = tupla[1]
            elif tupla[0] < menor_dist:
                menor_dist = tupla[0]
                vogal_proxima = tupla[1]

        nova_p += vogal_proxima

        while True:
            idx_prox_consoante = idx_consoante + 1
            if idx_prox_consoante == len(alfa):
                nova_p += 'z'
                break
            elif alfa[idx_prox_consoante] in vogais:
                idx_prox_consoante += 1
                nova_p += alfa[idx_prox_consoante]
                break
            else:
                nova_p += alfa[idx_prox_consoante]
                break

print(nova_p)






"""  
            if distancia < menor_dist:
                v_mais_prox = idx_vogal
                menor_dist = distancia
            
            elif distancia == menor_dist:
                if v_mais_prox > idx_vogal:
                    v_mais_prox = idx_vogal
                    menor_dist = distancia
        
        nova_p += alfa[v_mais_prox]
        prox_letra = idx_consoante + 1
        while True:
            if prox_letra == len(alfa):
                nova_p += 'z'
                break
            elif alfa[prox_letra] not in vogais:
                nova_p += alfa[prox_letra]
                break
            else:
                prox_letra += 1
print(nova_p)
"""