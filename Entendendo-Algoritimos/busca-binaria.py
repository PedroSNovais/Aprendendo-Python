def busca_binaria_numeros(lista: list, alvo: int) -> int:
   """
   Realiza busca binaria em uma lista de numeros ordenada. 
 
   parametros:
      lista (list): Lista de numeros inteiros ordenada.
      alvo (int): Numero a ser buscado na lista.
   return
      int: Indice do numero alvo na lista ou -1 se nao encontrado.
   """
   baixo = lista[0] 
   alto = lista[len(lista)-1]
   while baixo <= alto:      
      chute = ( alto + baixo ) // 2
      if alvo > chute:
         baixo = chute + 1
      elif chute == alvo:
         return lista.index(chute)
      else:
         alto = chute - 1
   return -1

# testando
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
numero = int(input("Digite um numero para procurar: "))
print(f'o indice do numero {numero} é {busca_binaria_numeros(lista, numero)}')
