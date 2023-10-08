# Aula 31 - Exercício guiado com while
"""
Iterando strings com while
"""
#        012345678910
# nome = 'Flavio Rodrigo'  # Iteráveis
#        1110987654321


nome = 'Flavio Rodrigo'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)