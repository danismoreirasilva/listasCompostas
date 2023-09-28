'''Faça um programa onde o usuário possa digitar sete valores inteiros e
insira em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente'''

listaNum = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor inteiro: '))
    if num % 2 == 0:
        listaNum[0].append(num)
    else:
        listaNum[1].append(num)
print(listaNum)
listaNum[0].sort()
listaNum[1].sort()
print(f'Os números pares são: {listaNum[0]}')
print(f'Os números ímpares são: {listaNum[1]}')