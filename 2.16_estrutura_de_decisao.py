#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas
#sequintes situações:
# a) Se o usuário informar A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
#os demais valores, sendo encerrado.
# b) Se o delta calculado for negativo, a equação não possui raizes reais; informe ao usuário e encerre o programa
# c) Se o delta calculado for igual a 0, a equação possui apenas uma raiz real; informe-a ao usuário
# d) Se o delta for positivo, a equação possui duas raizes reais; informe-as ao usuário.

from math import sqrt
print('=+'*23)
print('PROGRAMA EQUAÇÃO DE SEGUNDO GRAU'.center(46))
print('=+'*23)
a = float(input('Valor de A: '))
if a != 0:
    b = float(input('Valor de B: '))
    c = float(input('Valor de C: '))
    delta = b**2 - 4*a*c
    print(f'Delta --> [{delta}]')
    if delta < 0:
        print('A equação não possui raizes reais')
    elif delta == 0:
        x = (b * -1) / 2*a
        print(f'S = [{x}]')
    else:
        xa = (-(b) + sqrt(delta)) / (2 * a)
        xb = (-(b) - sqrt(delta)) / (2 * a)
        print(f'S = [{xa:.2f} , {xb:.2f}]')
else:
    print('A = 0 - NÃO É UMA EQUAÇÃO DE 2º GRAU')