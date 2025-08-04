responsavel = str(input("Digite o nome do responsavel pela reserva: ").strip().capitalize())
if responsavel.isalpha():
    print(responsavel)
else:
    print("Erro. Digite um nome valido !")
    quit()

print("-=" * 20)
diaIn = int(input("Digite o dia do check-in: "))
mesIn = int(input("Digite o mês do check-in: "))
anoIn = int(input("Digite o ano do check-in: "))
print("-=" * 20)
diaOut = int(input("Digite o dia do check-out: "))
mesOut = int(input("Digite o mês do check-out: "))
anoOut = int(input("Digite o ano do check-out: "))
print("-=" * 20)

# Definindo preços
tipos = ("Luxo", "Standard", "Premium")
print(tipos)
quarto = str(input("Digite o tipo de quarto: ").strip().capitalize())    
if quarto == tipos[0]:
    print(tipos[0])
    valor = int(250)

elif quarto == tipos[1]:
    print(tipos[1])
    valor = int(100)

elif quarto == tipos[2]:
    print(tipos[2])
    valor = int(180)

else:
    print("Erro! Digite um tipo de quarto valido")
    quit()

# Validação dos dados
if anoOut < anoIn or anoIn // 1000 < 2: # ano de saida maior que de entrada ou ano escrito com menos de 4 digitos
    print("Erro. Existe incongruencia nas datas: Ano abaixo de 2000!")
    quit()
elif (mesIn > 12 or mesOut > 12) or (mesIn < 1 or mesOut < 1): # mais que 12 meses
    print("Erro. Existe incongruencia nas datas: Meses inexistentes !")
    quit()
elif anoIn == anoOut and mesOut < mesIn: # anos iguais
    print("Erro. Existe incongruencia nas datas !")
    quit()
elif anoIn == anoOut and mesIn == mesOut and diaOut < diaIn:
    print("Erro. Existe incongruencia nas datas !")
    quit()
elif 30 < diaIn < 1 or 30 < diaOut < 1:
    print("Erro. Digite dias validos !")
    quit()
elif diaIn == diaOut and mesIn == mesOut and anoIn == anoOut:
    print("Erro: Você não pode entar e sair no mesmo dia")
    quit()
    
# calculando dias
if anoIn == anoOut:
    diasCorridos = 30*(mesOut - mesIn) + diaOut - diaIn
elif anoOut == anoIn +1:
    diasCorridos = 30*(mesOut + (12 - mesIn)) + diaOut - diaIn
else:
    diasCorridos = (anoOut * 365 + mesOut * 30 + diaOut) - (anoIn * 365 + mesIn * 30 + diaIn)
    
valortotal = valor*diasCorridos
print("--" * 20)
print(f"Responsavel pela reserva: {responsavel}")
print(f'Dia de check-in: {diaIn}/{mesIn}/{anoIn}')
print(f'Dia de check-out: {diaOut}/{mesOut}/{anoOut}')
print(f'O quarto reservado foi {quarto} por {diasCorridos} dias')
print(f'O valor total foi de R${valortotal}')
