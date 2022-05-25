#Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado acompanhado de uma frase que diga se o número é:
# a) par ou impar
# b) positivo ou negativo
# c) inteiro ou decimal

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
print('[1] - Soma')
print('[2] - Subtração')
print('[3] - Multiplicação')
print('[4] - Divisão')
op = int(input('Escolha uma Operação: '))
if op == 1:
    result = n1 + n2
    top = f'{n1} + {n2} = {n1 + n2}'
elif op == 2:
    result = n1 - n2
    top = f'{n1} - {n2} = {n1 - n2}'
elif op == 3:
    result = n1 * n2
    top = f'{n1} x {n2} = {n1 * n2}'
else:
    result = n1 / n2
    top = f'{n1} / {n2} = {n1 / n2}'
if result % 1 == 0 and result % 2 == 0:
    conj = 'INTEIRO'
    pi = 'PAR'
    if result >= 0:
        sinal = 'POSITIVO'
    else:
        sinal = 'NEGATIVO'
    print('#' * 100)
    print(f'{top} --> O resultado da operação é um número {conj}, {pi} e {sinal}')
else:
    conj = 'DECIMAL'
    if result > 0:
        sinal = 'POSITIVO'
    else:
        sinal = 'NEGATIVO'
    print('#' * 100)
    print(f'{top} --> O resultado da operação é um número {conj} e {sinal}')

