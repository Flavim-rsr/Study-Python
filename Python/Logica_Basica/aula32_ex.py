# Aula 32 - Exercício guiado - Calculadora 

'''Calculadora com while'''

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None     # Criando uma flag para marcar a variavel 
    num_1 = 0
    num_2 = 0
    try:
        num_1 = float(numero_1)   # Convertendo o str do input para numero float  
        num_2 = float(numero_2)   # Convertendo o str do input para numero float
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue    # Caso o usuario digite numeros invalidos o continue vai jogar ele para o topo do programa novamente

    operadores_permitidos = '+-/*'  # Variavel com os operadores permitidos

    if operador not in operadores_permitidos:   # Validação caso o usuario digite operador invalido
        print('Operador inválido.')
        continue    # Caso o usuario digite numeros invalidos o continue vai jogar ele para o topo do programa novamente

    if len(operador) > 1:   # Validação caso o usuario digite mais de um operador
        print('Digite apenas um operador.')
        continue    # Caso o usuario digite numeros invalidos o continue vai jogar ele para o topo do programa novamente
    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{num_1} + {num_2} = ',num_1 + num_2)
    elif operador == '-':
        print(f'{num_1} - {num_2} = ',num_1 - num_2)
    elif operador == '*':
        print(f'{num_1} * {num_2} = ',num_1 * num_2)
    elif operador == '/':
        print(f'{num_1} / {num_2} = ',num_1 / num_2)
    else:
        print('Nunca deveria chegar aqui') # Validação caso chegue aqui o codigo tem um erro
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break