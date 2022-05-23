#Faça um programa que peça dois números e imprima o maior deles

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
if n1 > n2:
    print(f'O maior valor digitado foi o primeiro valor = [{n1}]. ')
elif n2 > n1:
    print(f'O maior valor digitado foi o segundo valor = [{n2}].')
else:
    print(f'Os valores digitados são equivalentes = [{n1}]')