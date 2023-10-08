# Aula 26 - Exercícios 

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num1 = input("Digite um número: ")     # A entrada do input sempre será em string

try:
    num = int(num1)     # Transformando a string do input em numero inteiro usando uma nova variavel
    if num % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é impar')
except:
    print("Você não digitou um número inteiro")

# Outra forma de fazer:
'''
num1 = input("Digite um número: ")

if num1.isdigit():  # Função que só aceita a entrada de números
    num = int(num1)
    if num % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é impar')
else:
    print("Você não digitou um número inteiro")
'''
#-------------------------------------------------------------------------
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Informe quantas horas são na sua cidade: ')       # A entrada do input sempre será em string
try:
    hora = int(horario)   # Transformando a string do input em numero float usando uma nova variavel
    manha = hora >= 0 and hora < 11    
    tarde = hora >= 12 and hora < 17
    noite = hora >= 18 and hora < 23
    if manha:
        print('Bom Dia!')
    elif tarde:
        print('Boa Tarde!')
    elif noite:
        print('Boa Noite!')
except:
    print('Digite somente numeros inteiros')
#-------------------------------------------------------------------------
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)    # Variavel para saber se ele digitou mais de um caracter
curto = len(nome) <= 4
normal = len(nome) >= 5 and len(nome) <= 6
grande = len(nome) > 6

if tamanho_nome > 1:
    if curto:
        print('Seu nome é curto')
    elif normal:
        print('Seu nome é normal')
    elif grande:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')