#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

maior = 0
menor = 0
cont = 0
soma = 0
while True:
    numero = float(input(f'Digite o {cont+1}º valor (0 a 1000):  '))
    while numero < 0 or numero > 1000:
        numero = float(input(f'NÚMERO INVÁLIDO! Digite um valor entre 0 e 1000: '))
    soma += numero
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    cont += 1
    perg = str(input('Deseja continuar digitando? [S]im | [N]ão: ')).upper()
    while perg not in 'SN':
        perg = str(input('RESPOSTA INVÁLIDA! Deseja continuar? [S]im ou [N]ão: ')).upper()
    if perg == 'N':
        break
print('-'*45)
print(f'Foram digitados {cont} números.'.center(45))
print(f'A soma entre eles é igual a: {soma}'.center(45))
print(f'O maior número digitado foi: {maior}'.center(45))
print(f'O menor número digitado foi: {menor}'.center(45))
print('-'*45)