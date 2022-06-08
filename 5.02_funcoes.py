#Faça um programa para imprimir:
# 1
# 1     2
# 1     2       3
#.....
# 1     2       3       n
#para um número informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a é-nesima linha.

def imprimeLinha(numero):
    for c in range(1, numero+1):
        print(f'{c}', end=' ')
    print()


def imprimeSequencia(numero):
    for numero in range(numero + 1):
        imprimeLinha(numero)


numero = int(input('Digite o número de linhas desejado: '))
imprimeSequencia(int(numero))


