#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de nu´meros pares
#e a quantidade de números ímpares.

cont_par = 0
cont_impar = 0
for n in range(1,11):
    numero = int(input(f'Digite o {n}º número inteiro: '))
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print(f'Foram digitados {cont_par} números pares e {cont_impar} números ímpares.')
