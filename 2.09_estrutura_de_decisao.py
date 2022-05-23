#Faça um programa que leia três números e mostre-os em ordem descrescente

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
if n1 >= n2 and n1 >= n3:
    if n2 > n3:
        print(f'{n1} | {n2} | {n3}')
    else:
        print(f'{n1} | {n3} | {n2}')
elif n2 >= n1 and n2 >= n3:
    if n1 > n3:
        print(f'{n2} | {n1} | {n3}')
    else:
        print(f'{n2} | {n3} | {n1}')
else:
    if n1 > n2:
        print(f'{n3} | {n1} | {n2}')
    else:
        print(f'{n3} | {n2} | {n1}')
