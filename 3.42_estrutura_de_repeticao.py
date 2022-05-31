#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles
#estão nos seguintes intervalos: [0- 25], [26 - 50], [51 - 75], e [76 - 100]. A entrada de dados 7
#deverá terminar quando for lido um número negativo.

i25 = 0
i50 = 0
i75 = 0
i100 = 0
while True:
    print('Digite abaixo um número de 0 a 100: (Para sair digite um número negativo.)')
    numero = int(input('Número: '))
    if numero > 100:
        numero = int(input('Digite um número Válido: '))
    if numero < 0:
        break
    if numero <= 25:
        i25 += 1
    elif numero <= 50:
        i50 += 1
    elif numero <= 75:
        i75 += 1
    else:
        i100 += 1
print(f'[ 0 -  25] --> \t{i25}')
print(f'[25 -  50] --> \t{i50}')
print(f'[51 -  75] --> \t{i75}')
print(f'[76 - 100] --> \t{i100}')
