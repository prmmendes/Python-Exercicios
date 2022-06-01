#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
#soma dos quadrados dos elementos do vetor.

numeros = []
numeros_pot = []
soma = 0
for n in range(10):
    num = int(input(f'{n+1}º número: '))
    numeros.append(num)
    numeros_pot.append(num**2)
for i, n in enumerate(numeros_pot):
    if i < len(numeros_pot) - 1:
        print(f'{n} + ', end='')
    else:
        print(f'{n} = ', end='')
print(sum(numeros_pot))