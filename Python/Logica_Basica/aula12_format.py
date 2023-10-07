# Aula 12 - Formatação de strings com o metodo format

a = "A"
b = "B"
c = 1.1
# Quando deixa as chaves vazias o python puxa na ordem das variaveis
#string = 'a = {} \nb = {} \nc = {:.2f}'
#string = 'a = {0} \nb = {1} \nc = {2:.2f}'
#formato = string.format(a,b,c) 
# Parametro nomeado = dar nome as chamada ou criação das funções
# Depois de criar um parametro nomeado, todos os outros apos ele precisam ser parametros nomeados tambem
# Os valores dos parametros são chamados de argumentos: nome2 = b

string = 'a = {nome1} \nb = {nome2} \nc = {nome3:.2f}'
formato = string.format(nome1 =a,nome2 = b,nome3 = c) 
print(formato)