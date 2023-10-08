# Aula 22 - Exercicio
'''
Peça ao usuario para digitar seu nome e sua idade
Se o nome e a idade forem digitados, exiba:
- Seu nome é {nome}
- Seu nome invertido é {nome invertido}
- Seu nome tem {n} letras
- A primeira letra do seu nome é {letra}
- A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade, exiba:
- "Desculpe, você deixou campos vazios"
'''
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:  # Caso o usuario deixe algum sem preencher não entra na condição
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')