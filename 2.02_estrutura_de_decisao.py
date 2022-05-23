#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite um número inteiro qualquer (positivo ou negativo): '))
if num > 0:
    print(f'O valor [{num}] é um valor POSITIVO')
elif num < 0:
    print(f'O valor [{num}] é um valor NEGATIVO')
else:
    print(f'O valor digitado foi [{num}]')

