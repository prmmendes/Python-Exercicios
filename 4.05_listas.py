#Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR,
#e os vetores IMPARES no vetor impar. Imprima os três vetores.

numeros = list()
pares = list()
impares = list()
for n in range (0, 20):
   num = int(input(f'{n+1}º Número: '))
   numeros.append(num)
   if num % 2 == 0:
       pares.append(num)
   else:
       impares.append(num)
print('Números Digitados         -->', end=' ')
for n in numeros:
    print(n, end=' ')
print()
print('Números Pares Digitados   -->', end=' ')
for p in pares:
    print(p, end=' ')
print()
print('Números Impares Digitados -->', end=' ')
for i in impares:
    print(i, end=' ')