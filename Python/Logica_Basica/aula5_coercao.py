# Aula 5 -  Coerção de tipos (convertendo um tipo para outro)

'''
Conversão de tipos, coerção
Type convertion, typecasting, coercion
É o ato de converter um tipo em outro
Tipos imutaveis e primitivos: 
str, int, float, bool 

'''
print(int("1") + 1, type(int("1"))) # Coerção de string para inteiro
print(float("1") + 2) # Coerção de string para float
print(bool(" "), type(bool(" ")))
print(str(11) + "b")
print("a" + "b") # Concatenação


# Caso duvida no tipo da variavel usar o type para saber qual seu tipo