'''Faça um programa que leia o nome e o peso de várias pessoas,
guardando os dados em uma lista. No final apresente:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves'''

dado = []
pessoas = []
maior = menor = 0
i = 1
while True:
    nome = str(input(f'{i}º Nome: ')).title()
    peso = float(input(f'{i}º Peso: '))

    dado.append(nome)
    dado.append(peso)
    pessoas.append(dado[:])
    dado.clear()
    i += 1

    while True:
        resp = str(input('Deseja continuar? s ou n:  ')).lower().strip()
        if resp in 'sn':
            break
        else:
            print('Erro: Você deve digitar somente s ou n!')

    if resp == 'n':
        break
print('='*40)
maior = menor = pessoas[0][1]
for p in pessoas:
    if p[1] >= maior:
        maior = p[1]
    if p[1] <= menor:
        menor = p[1]

print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso é: {maior}kg. As pessoas mais pesadas são: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=',')

print(f'\nO menor peso é: {menor}kg. As pessoas menos pesadas são: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=',')