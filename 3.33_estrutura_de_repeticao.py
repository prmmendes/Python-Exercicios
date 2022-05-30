#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto
#indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como
#a média das temperaturas

cont = 0
soma_temp = 0
while True:
    temp = float(input('Informe a Temperatura em ºC - (Digite (-)274 para Sair: ' ))
    if temp <= -274:
        break
    cont += 1
    temperatura = temp
    soma_temp += temperatura
    if cont == 1:
        maior = temperatura
        menor = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
print(f'Maior Temperatura Cadastrada: {maior}ºC')
print(f'Menor Temperatura Cadastrada: {menor}ºC')
print(f'A média das Temperaturas Cadastradas: {(soma_temp / cont):.1f}ºC')


