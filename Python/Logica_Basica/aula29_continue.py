# Aula 29 - while + continue - pulando alguma repetição

contador = 0
while contador <= 100:
    contador += 1
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue    # Quando o programa chega no continue ele volta pro começo sem executar oque está baixo
    if contador >= 10 and contador <= 27:
        continue 
    print(contador)  
    if contador == 40:
        break       # Quando o programa chega no break ele para a repetição