#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores

soma = 0
cont = 0
while True:
    numero = float(input(f'Digite o {cont+1}º valor: '))
    soma  = soma + numero
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    cont += 1
    perg = str(input('Deseja continuar digitando? Digite [N] para Não ')).upper()
    if perg == 'N':
        break
print(f'Foram digitados {cont} números. E a soma entre eles é igual a {soma}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
