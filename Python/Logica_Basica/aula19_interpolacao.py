# Aula 19 - Interpolação de string com % em Python

'''

Interpolação básica de strings 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

'''

nome = 'Flavio'
preco = 100.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %4x' %  (1500,1500)) # x para minusculo
print('O hexadecimal de %d é %8X' %  (1500,1500)) # X para maisculo