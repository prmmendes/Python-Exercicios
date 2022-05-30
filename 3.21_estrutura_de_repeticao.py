#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input('Digite um número para verificar se é primo: '))
cont = 0
aux = numero
while aux >= 1:
    rest = numero % aux
    if rest == 0:
        cont += 1
    aux -= 1
if cont <= 2:
    print(f'O número {numero} É PRIMO!')
else:
    print(f'O número {numero} NÃO É PRIMO!')