hora_inicio, min_inicio, hora_fim, min_fim = (int(i) for i in input().split())

inicio = hora_inicio * 60 + min_inicio
fim = hora_fim * 60 + min_fim

if fim <= inicio:
    fim += 24 * 60

tempo_total = fim - inicio
print(f"O JOGO DUROU {tempo_total // 60} HORA(S) E {tempo_total % 60} MINUTO(S)")
