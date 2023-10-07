# Aula 18 - Operadores in e not in

'''

Operadores in(está entre) e not in (não está entre)
Strings são iteráveis = navegar item por item
  0 1 2 3 4 5 
  F l a v i o
 -6-5-4-3-2-1

'''

nome = 'Flávio'
print(nome[2])
print(nome[-5])
print(10 * '-') # Separador
print('á' in nome)
print('z' in nome)
print(10 * '-') # Separador
print('á' not in nome)
print('z' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')