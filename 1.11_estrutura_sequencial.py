#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
f1 = float(input('Digite um número real: '))
print(f'A) O dobro de {n1} é igual a {n1*2} | A metade de {n2} é igual a {n2/2} | Seu produto é igual a {(n1*2)*(n2/2)}')
print(f'B) O triplo de {n1} é igual a {n1*3} | A soma de {n1*3} + {f1} é igual a {n1*3+f1}')
print(f'C) {f1}³ é igual a {f1*f1*f1}')