# Aula 16 - Exercício de programação com if e comparação


valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor: ')
# Transformar as variaveis em int em uma nova variavel e depois da entrada, para não ter erros de valores literais str
num1 = int(valor_1)
num2 = int(valor_2)

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print('Os dois valores são iguais')