#Faça um programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
cont = 1
maior = 0
menor = 0
if cont == 1:
    maior = n1
    menor = n1
    cont +=1
if n2 >= n1 and n2 >= n3:
    maior = n2
elif n3 >= n2 and n3 >= n1:
    maior = n3
else:
    maior = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
elif n3 <= n2 and n3 <= n1:
    menor = n3
else:
    menor = n1
print(f'Maior valor digitado foi: [{maior}]')
print(f'Menor valor digitado foi: [{menor}]')