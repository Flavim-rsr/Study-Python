# Aula 13 - Usando a função input para coletar dados do usuário

nome = input ('Qual o seu nome? ')  #Função input retorna str
print(f'O seu nome é {nome=}')  #nome = retorna oque tem na variavel nome 
numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')
int_num = int(numero_1)     #transformar a str em int somente depois da entrada dos dados, para evitar erros de entrada com valores literais
int_num2 = int(numero_2)
print(f'A soma dos numero é: {int_num + int_num2}')