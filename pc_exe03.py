'''Faça um programa que crie uma matriz de ordem 3, e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta (mxn)'''

matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite o valor [{i},{j}]: ')))

for linha in matriz:
    for j in linha:
        print(f'[{j}]',end='')
    print()

