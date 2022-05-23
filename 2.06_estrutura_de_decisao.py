#Faça um programa que leia três números e mostre o maior deles

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
cont = 1
maior = 0
if cont == 1:
    maior = n1
    cont += 1
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
print(f'O maior valor digitado foi: [{maior}]')
