# Aula 23 - Introdução ao try e except para capturar erros (exceptions)

"""
Introdução ao try/except
try ->  tentar executar o codigo
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('Vou dobrar o numero que você digitar: ')
try:
    
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2.:2}')
except:
    print('Isso não é um número')