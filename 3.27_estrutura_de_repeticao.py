#Faça um programa que calcule o número médio de alunos por turma. Para isso, peça a quantidade de turmas,
#e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input('Número de Turmas: '))
soma_alunos = 0
for c in range(1, turmas + 1):
    alunos = int(input(f'Quantidade de alunos na Turma {c}: '))
    while alunos < 0 or alunos > 40:
        alunos = int(input(f'Uma turma não pode ser maior que 40 alunos. Digite a quantidade correta: '))
    soma_alunos += alunos
print(f'Foram cadastradas {turmas} Turmas.')
print(f'No Total somam {soma_alunos} Alunos.')
print(f'A média de alunos por turma é {(soma_alunos / turmas).__ceil__()} alunos')