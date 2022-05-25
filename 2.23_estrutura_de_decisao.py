#Faça um programa que peça um número e informe se o número é inteiro ou decimal.

numero = float(input('Número: '))
if numero % 1 == 0:
    print(f'O número {numero} é INTEIRO')
else:
    print(f'O número {numero} é DECIMAL')