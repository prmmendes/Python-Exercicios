#Faça um programa que leia um vetor de 5 números inteiros e mostre-os

lista = list()
for c in range (1, 6):
    numero = int(input(f'Digite o {c} número: '))
    lista.append(numero)
print('Lista --> ', end=' ')
for m in lista:
    print(f'{m}', end=' ')