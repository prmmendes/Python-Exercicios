#Faça um Programa que peça as quatros notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0

medias_alunos = []
maiores_medias = 0

for aluno in range(1, 11):
    soma_notas = 0
    for nota in range(1, 5):
        nota = float(input(f'Aluno {aluno:>2}| Nota{nota}: '))
        while nota < 0 or nota > 10:
            nota = float(input(f'NOTA INVÁLIDA! NOTA DEVE SER DE 0 A 10 - Aluno {aluno:>2}| Nota{nota}: '))
        soma_notas += nota
        media = soma_notas / 4
    medias_alunos.append(media)
    if media >= 7:
        maiores_medias += 1
    print(f'Média do Aluno {aluno}: {media:.2f}')
    print('-' * 30)
print(f'{maiores_medias} Alunos tiveram notas acima ou igual a 7')



