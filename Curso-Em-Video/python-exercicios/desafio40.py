from time import sleep
print(f'{"Desafio 40":=^30}')
n1 = float(input('Digite a nota de um aluno: '))
n2 = float(input('Digite a segunda nota de um aluno:'))
n3 = float(input('Digite a terceira nota:'))
media = (n1 + n2 + n3) / 3
print(f'A media do aluno é {media:.1f}')
sleep(1.5)
if media < 6:
    print(f' Com a media de {media:.1f} o aluno está \033[1;31mREPROVADO\033[m')
elif 6 <= media < 7:
    print(f'Com media de {media:.1f} aluno esta de \033[1;33mRECUPERAÇÃO\033[m')
elif media > 7:
    print(f'Com media {media:.1f} o aluno fou \033[1;32mAPROVADO\033[m ')
