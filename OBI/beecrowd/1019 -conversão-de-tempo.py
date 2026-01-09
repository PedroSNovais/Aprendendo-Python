segundos = int(input())

minutos = segundos // 60
hora = minutos // 60

segundos = segundos % 60
minutos = minutos % 60

horario = [hora, minutos, segundos]
cont = 0
for i in horario:
    if cont == 2:
        print(i)
    else:
        print(f'{i}:', end = '')
    cont += 1