# Aula 27 - Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string

"""
Documentação Python: https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
# Forma de mudar uma variavel imutavel
string = 'Flavio Rodrigo'
outra_string = (f'{string[:3]}ABC{string[4:]}')
print(string)
print(outra_string)
print(string.zfill(50))     # Função que preenche de zeros a esquerda totalizando a quandidade de caracteres que você digitar