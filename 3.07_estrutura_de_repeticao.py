#Faça um programa que leia 5 números e informe o maior número.

for n in range(1, 6):
    numero = int(input(f'Digite o {n}º número: '))
    if n == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero
        else:
            maior = maior
print(f'O maior número digitado foi --> {maior}')

