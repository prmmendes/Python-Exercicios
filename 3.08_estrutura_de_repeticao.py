#Faça um programa que leia 5 números e informe a soma e a média dos números

soma = 0
for n in range(1, 6):
    numero = int(input(f'Digite o {n}º número: '))
    soma = soma + numero
print(f'A soma dos números digitados foi  --> {soma}')
print(f'A média dos números digitados foi --> {soma/5}')