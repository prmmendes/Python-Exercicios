#Faça um programa para imprimir:
# 1
# 2     2
# 3     3       3
# .........
# n     n       n       n       n
#para um n informado pelo usuário. Use a função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimirPiramide(linhas):
    for c in range(1, linhas + 1):
        cont = 1
        while True:
            print(f'{c:>2}', end='    ')
            if cont == c:
                break
            cont += 1
        print()

n = int(input('Digite a quantidade de linhas desejadas: '))
imprimirPiramide(n)




