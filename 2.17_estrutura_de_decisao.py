#Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este
#ano é ou não bissexto

from time import sleep
ano = int(input('Ano: '))
print('Analisando se ano é bissexto...')
sleep(2)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')

