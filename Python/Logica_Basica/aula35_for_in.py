# Aula 35 - Introdução ao for / in - estrutura de repetição para coisas finitas

texto = 'Python'
# for é utilizado quando sabemos a quantidade de repetições que precisamos
i = 0
novo_texto = ''
tamanho_string = len(texto)
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)