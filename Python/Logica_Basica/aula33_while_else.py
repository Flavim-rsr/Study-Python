# Aula 33 - while / else (recurso peculiar do Python)

string = 'Valorqualquer'
i = 0

# break = quando utilizamos o break o else no final não é executado
# toda vez que o laço while vai até o final, o else é executado
# usado para procurar algo dentro da repetição

while i <  len(string):
    letra = string[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else: 
    print('Não encontrei espaço na string')
print('Fora do while')