segundos = int(input())

minutos = segundos // 60
hora = minutos // 60

segundos = segundos % 60
minutos = minutos % 60

print(f'{hora}:{minutos}:{segundos}')