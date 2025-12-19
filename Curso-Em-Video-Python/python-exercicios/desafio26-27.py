# desafio 26
print(f'\033[4;30;45m{"Desafio 26":=^30}\033[m')
frase = str(input('Digite uma frase: '))
frase.strip()
frase.lower()
A = frase.count('a')
print(f'A letra "A" aparece \033[30;44m{A} vezes\033[m na sua frase.')
print(f'A primeira vez aparece na posição {frase.find("a")+1} e a ultima vez na {frase.rfind("a")+1}')

# Desafio 27
print(f'\033[1;30;46m{"Desafio 27":=^30}\033[m')
nomec = str(input('Digite seu nome completo: ')).strip()
nomec = nomec.title()
nomec = nomec.split()
print(f'\033[1;30;44mÉ um prazer te conhecer !!\033[m')
print(f'Seu primeiro nome é \033[1;34;40m{nomec[0]:-^12}\033[m.')
print(f'E Seu ultimo nome é \033[1;34;40m{nomec[len(nomec)-1]:-^12}\033[m.')
