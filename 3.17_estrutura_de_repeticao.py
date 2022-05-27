#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

fatorial = int(input('Fatorial de: '))
aux = fatorial
for n in range(fatorial-1, 0, -1):
    fatorial = fatorial * n
print(f'{aux}! = ', end='')
for n in range(aux, 0, -1):
    if n > 1:
        print(f'{n} x ', end='')
    else:
        print(f'{n} = ', end='')
print(fatorial)


