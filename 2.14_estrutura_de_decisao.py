#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um
#semestre, e calcule a sua média. A atribuição de conceitos obedece a tabela abaixo:
# Entre 9 e 10 - A
# Entre 7.5 e 9 - B
# Entre 6 e 7.5 - C
# Entre 4 e 6 - D
# Entre 4 e zero - E
# O algoritmo deve mostrar na tela as notas, a média, o conceito, e a mensagem 'Aprovado' se o conceito for A, B,
#ou C ou 'Reprovado' se o conceito for D ou E.

nome = str(input('Aluno: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2)/2
if media >= 9 and media <= 10:
    conceito = 'A'
    situacao = 'APROVADO'
elif media >= 7.5 and media < 9:
    conceito = 'B'
    situacao = 'APROVADO'
elif media >= 6 and media < 7.5:
    conceito = 'C'
    situacao = 'APROVADO'
elif media >= 4 and media < 6:
    conceito = 'D'
    situacao = 'REPROVADO'
elif media >= 0 and media < 4:
    conceito = 'E'
    situacao = 'E'
else:
    conceito = 'DADOS INVÁLIDOS'
    situacao = 'DADOS INVÁLIDOS'
print(f'Nome do Aluno: {nome}')
print(f'Nota 1 - {n1} | Nota 2 - {n2}')
print(f'Média das Notas: {media}')
print(f'Conceito do Aluno: {conceito}')
print(f'Situação do Aluno: {situacao}')