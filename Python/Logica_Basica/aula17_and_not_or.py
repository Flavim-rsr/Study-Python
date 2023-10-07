# Aula 17 - and (e), or (ou) e not (não)

# Operadores Logicos

'''

and:
-Todas as condições precisam ser verdadeiras 
-Se  qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
-São considerados falsy (que vc já viu) 0 0.0 '' False
-Também existe o tipo none que é usado para representar um não valor

''' 
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '1234'

# if True:
if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)

'''

or:
-Qualquer condição verdadeira avalia toda a expressão como verdadeira
-Se qualquer valor for avaliado verdadeiro, a expressão inteira é avaliada naquele valor
-São considerados falsy (que vc já viu) 0 0.0 '' False
-Também existe o tipo none que é usado para representar um não valor

'''

entrada2 = input('[E]ntrar [S]air: ')
senha2 = input('Senha: ')
senha_permitida2 = '123'

# Uso de parênteses dentro da condição para ser realizado primeiro
if (entrada2 == 'E' or 'e') and senha2 == senha_permitida2:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
senha_avaliacao = 0 or False or 'abc' or True
print(senha_avaliacao)  # Retorna true pois o ultimo valor encontrado foi o 'abc' = True

senha_X = input('Senha: ') or 'Sem senha'
print(senha_X)

'''

Operador lógico not 
Usado para inverter expressões
not True = False
not False = True

'''

print(not True) # False
print(not False) # True
