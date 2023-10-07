# Aula 21 - Fatiamento de strings e a função len

'''
Fatiamento de strings 
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
'''
# [inicio: fim: passo]
# Inicio é de onde o programa vai começar a exibir
# Fim é onde ele vai parar, caso omita o fim, ele exibe tudo
# Passo é de quantos em quantos caracteres ele vai pular

variavel = 'Olá Mundo'
print(variavel[4:])
print(variavel[-9:])
print(variavel[0:9:3])
print(variavel[::-1])   # Invertendo a str

# A função len retorna a quantidade de caracteres da str
print(len(variavel))