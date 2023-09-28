'''Aprimore o exercício anterior e mostre no final:
a) a soma de todos os valores digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaTotal = somaCol3 = maior2l = somaPares = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor [{i},{j}]: '))

for linha in matriz:
   somaTotal += sum(linha)

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]

for i in range(3):
    somaCol3 += matriz[i][2]

'''for i in range(3):
    if matriz[1][i] >= maior2l:
        maior2l = matriz[1][i]'''

print(f'A soma de todos valores é: {somaTotal}')
print(f'A soma de todos valores pares é: {somaPares}')
print(f'A soma de elementos da 3º coluna é: {somaCol3}')
#print(f'O maior elemento da 2º linha é: {maior2l}')
print(f'O maior elemento da 2º linha é: {max(matriz[1])}')