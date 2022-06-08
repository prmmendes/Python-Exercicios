#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma destes três argumentos.

def soma(a, b, c):
    s = a + b + c
    return s


a = int(input('1º Número: '))
b = int(input('2º Número: '))
c = int(input('3º Número: '))
print(f'Soma = {soma(a, b, c)}')