# Aula 2 - A função print

'''
Para mostrar na tela sempre usar print, e separar por virgulas

'''
# Print já da o espaço automatico entre os valores, caso queria um separador usar sep="-" 
# Como padrão de um print para o outro já tem uma quebra de linha no final, caso queira mudar use end=""
print(12,34,sep="-") 
print(77,22, end=" 55") 

"""
Python = Linfuagem de programação 
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
string são textos que estão dentro de aspas

"""
print(123)

# aspas simples
print('Flavio Rodrigo')
print(1,'Flavio "Rodrigo"') # maneira mais facil de colocar aspas dentro do codigo

# aspas duplas
print("Flavio Rodrigo")
print(1,"Flavio 'Rodrigo'") # maneira mais facil de colocar aspas dentro do codigo

# escape (usado para por outras aspas dentro do codigo)
print('Flavio \'Rodrigo')

# r (utilizado para expressões regulares)
print(r'Flavio \'Rodrigo') 