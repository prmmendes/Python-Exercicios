#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno, e o
#segundo representando sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número
#do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

n_aluno = 0
altura = 0
for a in range(1, 11):
    altura = int(input(f'Aluno {a} | Altura (cm): '))
    if a == 1:
        maior_altura = altura
        cod_maior = a
        menor_altura = altura
        cod_menor = a
    if altura > maior_altura:
        maior_altura = altura
        cod_maior = a
    if altura < menor_altura:
        menor_altura = altura
        cod_menor = a
print(f'O aluno nº {cod_maior} é o aluno mais alto da classe, medindo {maior_altura}cm')
print(f'O aluno nº {cod_menor} é o aluno mais baixo da classe, medindo {menor_altura}cm')