#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

from statistics import mean
notas = list()
for c in range(1,5):
    nota = float(input(f'Nota {c} [0 a 10]: '))
    while nota < 0 or nota > 10:
        nota = float(input(f'{nota} é uma Nota Inválida. Digite uma nota de 0 a 10: '))
    notas.append(nota)
media = mean(notas)
print(f'Média das Notas: {media:.1f}')
