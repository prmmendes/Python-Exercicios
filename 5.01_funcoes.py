#Faça um programa para imprimir:
# 1
# 2     2
# 3     3       3
# .........
# n     n       n       n       n

def imprimirPiramide(linhas):
    for c in range(1, linhas + 1):
        cont = 1
        while True:
            print(c, end='    ')
            if cont == c:
                break
            cont += 1
        print()

n = int(input('Digite a quantidade de linhas desejadas: '))
imprimirPiramide(n)




