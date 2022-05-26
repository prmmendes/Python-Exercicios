#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
#compreendido entre eles.

ni = int(input('Início: '))
nf = int(input('Fim: '))
for c in range(ni, nf+1):
    print(f'{c}', end=' ')