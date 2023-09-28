'''Crie um programa que leia o nome e duas notas de vários alunos, e a média das notas, e guarde tudo em uma lista composta.
No final, mostre o boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente'''

turma = []
aluno = []
status = ''
aprovados = reprovados = 0
while True:
    while True:
        nome = str(input('Digite o nome do aluno: ')).title().strip()
        if nome.isspace() or len(nome) == 0:
            print('Erro. O nome não pode ser vazio!')
        else:
            break

    while True:
        try:
            nota1 = float(input('Digite a 1º Nota: '))
            if 0 <= nota1 <= 10:
                break
            else:
                print('Erro. O valor da nota deve estar entre 0 e 10!')
        except Exception as e:
            print(f'Erro -> {e}')

    while True:
        try:
            nota2 = float(input('Digite a 2º Nota: '))
            if 0 <= nota2 <= 10:
                break
            else:
                print('Erro. O valor da nota deve estar entre 0 e 10!')
        except Exception as e:
            print(f'Erro -> {e}')

    media = (nota1 + nota2)/2
    if media >= 6:
        status = 'aprovado'
        aprovados += 1
    else:
        status = 'reprovado'
        reprovados += 1

    aluno = [nome, [nota1, nota2], media, status]
    turma.append(aluno[:])


    while True:
        resp = str(input('Deseja continuar: ')).lower().strip()
        if resp in 'sn':
            break
        else:
            print(f'Erro -> Digite s ou n!')

    if resp == 'n':
        break

print(f'{"Turma":=^56}')
print(f'{"ID":<4}{"Nome":<40}{"Média":>8}')
print('-'*56)
for i, v in enumerate(turma):
    #print(f'ID {i+1}° Aluno: {v[0]} - Média {v[2]}')
    print(f'{i+1:<4}{v[0]:<40}{v[2]:>8}')
print()

if aprovados > 0:
    print(f'{"Alunos Aprovados":=^56}')
    for i, v in enumerate(turma):
        if v[3] == 'aprovado':
            print(f'Aluno: {v[0]}, com a média {v[2]}.')
else:
    print('Todos os alunos foram reprovados!')
print()

if reprovados > 0:
    print(f'{"Alunos Reprovados":=^56}')
    for i, v in enumerate(turma):
        if v[3] == 'reprovado':
            print(f'Aluno: {v[0]}, com a média {v[2]}.')
else:
    print('Todos os alunos foram aprovados!')
print()

while True:
    while True:
        opc = int(input(f'Digite o ID do Aluno que deseja detalhar as notas: Os valores são de 1 até {len(turma)}:  '))
        if 1 <= opc <= len(turma):
            break
        else:
            print(f'Erro. Você deve digitar um valor de 1 até {len(turma)}')

    print(f'As notas do aluno {turma[opc-1][0]} são: {turma[opc-1][1]}')

    while True:
        resp = str(input('Deseja consultar as notas de mais algum aluno s/n: ')).lower().strip()
        if resp in 'sn':
            break
        else:
            print(f'Erro: Você só pode digitar s ou n')
    if resp == 'n':
        break

print(f'Você saiu do programa!')