# Aula 20 - Formatação de strings com f-strings

'''

Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o meu número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r __repr__, !s __str__ !a

'''

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:$^10}')
print(f'{1000.59858498:0=+10,.1f}') # Sinal de mais depois dos : somente para o python mostrar o sinal de mais na execução
print(f'O hexadecimal de 1500 é {1500:04X}') # X para maisculo
print(f'O hexadecimal de 1500 é {1500:08x}') # x para minusculo
print(f'{variavel!r}')