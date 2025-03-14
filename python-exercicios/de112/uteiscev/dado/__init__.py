def leiadinheiro(prompt):
    while True:
        valor = str(input(prompt))
        if '.' in valor:
            valor = valor.replace('.', '')
            print(valor)
        if valor.isnumeric():
            return float(valor)
            break
        else:
            print(f'\033[1;31mERRO! O valor "{valor}" não foi aceito!\033[m')
