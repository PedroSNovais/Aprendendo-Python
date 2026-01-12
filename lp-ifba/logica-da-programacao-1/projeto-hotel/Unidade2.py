from datetime import datetime


valorMedio = maiorReserva = maisCara = somaTotalValores = reservas = resposta = 0
quartosStandard = 10
quartosPremium = 5
quartosLuxo = 3
responsavelMaiorReserva = responsavelMaisCara = "NINGÉUM"

while(resposta != 2):
    codigo = True
    cancelar = 2
    # Sair do programa ?
    
    print("=-" * 30)
    print("1 - NOVA RESERVA \n2 - SAIR")
    resposta = (input("Digite o que deseja: "))
    print("=-" * 30)
    if not resposta.isnumeric():
        continue
    resposta = int(resposta)
    while(resposta != 2 and resposta !=1):
        print("=-" * 30)
        print("Digite um numero valido...")
        print("1 - NOVA RESERVA \n2 - SAIR")
        resposta = (input("Digite o que deseja: "))
        if not resposta.isnumeric():
            continue
        resposta = int(resposta)

        if resposta == 2 or resposta == 1:
            break
    if resposta == 2:
        break
    

    # Nome do responsavel
    responsavel = str(input("Digite o nome do responsavel pela reserva: ").strip().capitalize())
    if not responsavel.isalpha():
        print("Erro. Digite um nome valido !")
        print("Está reserva foi descontinuada !")
        continue


    # Definindo datas

    data_chekIn_str = str(input("Digite a data de check in: (dd/mm/aaaa) "))
    data_chekOut_str = str(input("Digite a data de check out: (dd/mm/aaaa) "))

    try: 
        data_chekIn = datetime.strptime(data_chekIn_str, "%d/%m/%Y")
    except ValueError:
        print("Erro! Data de check in invalida !")
        print("Está reserva foi descontinuada !")
        continue
    try: 
        data_chekOut = datetime.strptime(data_chekOut_str, "%d/%m/%Y")
    except ValueError:
        print("Erro! Data de check out invalida !")
        print("Está reserva foi descontinuada !")
        continue


    # calculando dias
    diasReserva = data_chekOut - data_chekIn
    diasReserva = diasReserva.days

    if diasReserva <= 0:
        print("Erro! Existe um equivoco nas datas ! ")
        print("Está reserva foi descontinuada !")
        continue


    # Definindo quartos
    codigo = True
    while codigo:
        tipos = ("Luxo", "Standard", "Premium")
        print("_-"*20)
        print(f"    {tipos}")

        cancelar = input("Deseja cancelar essa reserva aqui ? [1-Sim/ 2-Não] ")
        if cancelar.isnumeric():
            if int(cancelar) == 1:
                codigo = False
                continue
        else:
            continue
        quarto = str(input("Digite o tipo de quarto: ").strip().capitalize())   
        quantidadeQuartosDesejados = int(input("Digite a quantidade de quartos: "))

        if quantidadeQuartosDesejados <= 0:
            print("--"*20)
            print("Erro! Quatidade de quartos invalida !")
            print("Digite uma quantidade valida !!")
            print("--"*20)
            continue

        if quarto == tipos[0]:
            if quantidadeQuartosDesejados > quartosLuxo:
                print("--"*20)
                print("Erro! Quatidade de quartos indisponivel !")
                print("Digite uma quantidade valida !!")
                print("--"*20)
                continue
            else:
                quartosLuxo -= quantidadeQuartosDesejados
                codigo = False
            valor = int(250)
            

        elif quarto == tipos[1]:
            if quantidadeQuartosDesejados > quartosStandard:
                print("--"*20)
                print("Erro! Quatidade de quartos indisponivel !")
                print("Digite uma quantidade valida !!")
                print("--"*20)
                continue
            else:
                quartosStandard -= quantidadeQuartosDesejados
                codigo = False
            valor = int(100)


        elif quarto == tipos[2]:
            if quantidadeQuartosDesejados > quartosPremium:
                print("--"*20)
                print("Erro! Quatidade de quartos indisponivel !")
                print("Digite uma quantidade valida !!")
                print("--"*20)
                continue
            else:
                quartosPremium -= quantidadeQuartosDesejados
                codigo = False
            valor = int(180)

        else:
            print("--"*20)
            print("Erro! Digite um tipo de quarto valido !")
            print("--"*20)
            continue

    if int(cancelar) == 1:
        continue
    # calculando o preço
    valortotal = valor*diasReserva
    valortotal = valortotal*quantidadeQuartosDesejados

    print("--" * 20)
    print(f"Responsavel pela reserva: {responsavel}")
    print(f'Dia de check-in: {data_chekIn_str}')
    print(f'Dia de check-out: {data_chekOut_str}')
    print(f'Quantidade de darias: {diasReserva}')
    print(f'O tipo de quarto: {quarto}')
    print(f'Quantidade de quartos: {quantidadeQuartosDesejados}')
    print(f'Valor total da reserva: R${valortotal}')
    print("--" * 20)
    reservas += 1
    somaTotalValores += valortotal
    valorMedio = somaTotalValores / reservas 
    if valortotal > maisCara:
        maisCara = valortotal
        responsavelMaisCara = responsavel
    if diasReserva > maiorReserva:
        maiorReserva = diasReserva
        responsavelMaiorReserva = responsavel

print(f"=="*30)
print(f"{'ESTATISTICAS GERAIS':^60}")
print (f"Total de reservas: {reservas}")
print(f"Soma total do valor das reservas: R${somaTotalValores :.2f}")
print(f"Valor médio das reservas: R${valorMedio :.2f}")
print(f"A reserva mais cara custou R${maisCara :.2f} e o responsavel por ela foi {responsavelMaisCara}")
print (f"A reserva mais longa durou {maiorReserva} dias e o responsavel por ela foi {responsavelMaiorReserva}")

