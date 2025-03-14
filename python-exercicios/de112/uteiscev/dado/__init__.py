def leiadinheiro(prompt):
    while True:
        valor = str(input(prompt))
        valor2 = valor
        if '.' in valor:
            valor2 = valor.replace('.', '')
        if ',' in valor:
            valor2 = valor.replace(',', '')
        if valor2.isnumeric():
            return float(valor.replace(',', '.'))
            break
        else:
            print(f'\033[1;31mERRO! O valor "{valor}" não foi aceito!\033[m')
