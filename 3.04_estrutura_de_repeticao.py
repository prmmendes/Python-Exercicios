#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
#de 3% e que a população de B seja de 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
#programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse
#ou iguale a população do país B, mantidas as taxas de crescimento.


a = 80000
b = 200000
cont = 0
while a < b:
    a = a + (a * (3 / 100))
    b = b + (b * (1.5 / 100))
    cont += 1
print('*'*65)
print('População do País A ultrapassará a População do País B'.center(65))
print('*'*65)
print(f'População atual de A: {a.__ceil__()} habitantes')
print(f'População atual de B: {b.__ceil__()} habitantes')
print(f'Demorará {cont} anos para o País A ultrapassar o País B')
