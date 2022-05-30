#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#Ex: 5! = 5.4.3.2.1=120. A saída deve ser conforme o exemplo

fatorial = int(input('Fatorial de: '))
aux = fatorial
for n in range(fatorial-1, 0, -1):
    fatorial = fatorial * n
print(f'{aux}! = ', end='')
for n in range(aux, 0, -1):
    if n > 1:
        print(f'{n}.', end='')
    else:
        print(f'{n} = ', end='')
print(fatorial)
