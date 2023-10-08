# Aula 28 - while e break - Estrutura de repetição

'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

'''
# Loop infinito -> Quando um código não tem fim -> Ctrl + c = parar o loop (KeyboardInterrupt)

condicao = True
while condicao:
    nome = input('Qual o seu nome? \n')
    print(f'Seu nome é {nome}')
    if nome == 'Sair':
        break       # Função que para a condição while mais proxima
print('Acabou')

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1
print('Acabou')

'''
Operadores de atribuição:
= += -= *= /= //= **= %=
'''

contador2 = 0

while contador2 <= 100:
    contador2 += 1
    print(contador2)
print('Acabou')

