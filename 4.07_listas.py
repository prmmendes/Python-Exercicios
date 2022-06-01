#Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

from math import prod
numeros = []
for n in range(5):
    numeros.append(int(input(f'{n+1}º número: ')))
for i, n in enumerate (numeros):
    if i < len(numeros)-1:
        print(f'{n} + ', end='')
    else:
        print(f'{n} = ', end='')
print(sum(numeros))
for i, n in enumerate (numeros):
    if i < len(numeros)-1:
        print(f'{n} x ', end='')
    else:
        print(f'{n} = ', end='')
print(prod(numeros))