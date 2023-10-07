# Aula 11 - Exercicio calculo do IMC (indice de massa corporea) + ellipsis + f-strings (formatação de strings)

nome = "Flavio Rodrigo"
peso = 60
altura = 1.70
imc = peso / (altura*altura)   # IMC = peso / (altura x altura)

#print(nome, "tem", altura, "de altura, pesa", peso, "quilos e seu IMC é", imc)
# Formatação f-strings
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"Pesa {peso} kg, e seu IMC é de: {imc:.2}" # :. é para definir quantas casas decimais você quer no numero, pode adicionar virgulas tambem :,.2
print(linha_1)
print(linha_2)
# ... = placeholder ou ellipsis, é quando você não sabe oque usar na variavel, mas já deixa ela criada como vazia