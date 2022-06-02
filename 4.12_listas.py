#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais
#de 13 anos possuem altura inferior a média de altura desses alunos.

idades = []
alturas = []
cont = 0
for a in range(30):
    idades.append(int(input(f'{a+1} Idade: ')))
    alturas.append(float(input(f'{a+1} Altura: ')))
media_altura = sum(alturas)/30
for a in range(30):
    if idades[a] > 13 and alturas[a] < media_altura:
        cont += 1
print(f'Média de Altura: {media_altura:.2f}')
print(f'{cont} Alunos com mais de 13 anos estão abaixo da Média')



