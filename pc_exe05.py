'''Faça um programa que ajude um jogador da megasena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep
listaJogos = []
listaTemp = []

while True:
    try:
        n = int(input('Quantos jogos devem ser sorteados: '))
        break
    except Exception as e:
        print(f'Erro -> {e}')

for i in range(n):
    for j in range(6):
        while True:
            num = randint(1, 60)
            if num not in listaTemp:
                listaTemp.append(num)
                break
    listaTemp.sort()
    listaJogos.append(listaTemp[:])
    listaTemp.clear()

print(f'{"Sorteando os jogos":=^30}')
for i, jogo in enumerate(listaJogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(1)
print(f'{"Fim do sorteio":=^30}')

