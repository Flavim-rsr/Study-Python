# Aula 6 - Introdução a variaveis em Python

# Variaveis são usadas para salvar algo na memoria do computador
# PEP8: inicie variaveis com letras minusculas, pode usar numeros e underline _
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variavel)
# Uso: nome_variavel = expressão

nome_completo = "Flavio Rodrigo De Souza Ribeiro"
soma_dois_mais_dois = 2 + 2
int_um = int("1") # Evitar fazer repetições no codigo, manter somente um ponto para poder alterar, em vez de ter que alterar varios lugares 
print(int_um, type(int_um))
print(nome_completo,"\n", soma_dois_mais_dois)

nome = "Flavio"
idade = 21
maior_de_idade = idade >= 18
print("Nome:", nome, "\nIdade:", idade)
print("É maior?", maior_de_idade)