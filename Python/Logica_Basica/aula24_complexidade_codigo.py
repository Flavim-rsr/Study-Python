# Aula 24 - Parte 1: Variáveis, constantes e complexidade de código

"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

"""
velocidade = 61     # Velocidade atual do carro
local_carro = 90   # Local em que o carro está na estrada

RADAR_1 = 60    # Velocidade maxima do radar 1
LOCAL_1 = 100   # Local onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega 

# Barra invertida é uma quebra de linha no codigo, dizendo que ele tem continuidade
velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1
    
# Tentar pensar em formas de simplificar o seu codigo, evitar colocar muitas condições em um if, e fazer as condições dentro das variaveis usando os operadores logicos
if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')