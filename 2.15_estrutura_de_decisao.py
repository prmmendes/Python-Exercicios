#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
#ser um triângulo. Indique, caso os lados formemum triângulo, se o mesmo é: equilátero, isóceles ou escaleno

from time import sleep
a = float(input('Digite o valor da Reta A: '))
b = float(input('Digite o valor da Reta B: '))
c = float(input('Digite o valor da Reta C: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print(f'As retas --> a:0 {a} | b: {b} | c: {c} --- formam um TRIÂNGULO')
    print('-'*30)
    print('Aguarde! Verificando tipo de triângulo...')
    sleep(3)
    if a == b and b == c:
        print('Tipo: TRIÂNGULO EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Tipo: TRIÂNGULO ISÓCELES')
    else:
        print('Tipo: TRIÂNGULO ESCALENO')
else:
    print(f'As retas --> a:0 {a} | b: {b} | c: {c} --- NÃO formam um TRIÂNGULO')
