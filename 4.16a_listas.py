#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
#Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
#ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
#receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante:

salario_total = []
c300 = c400 = c500 = c600 = c700 = c800 = c900 = c1000 = cmais = 0
while True:
    perg = str(input('Deseja cadastrar funcionário? [S]im ou [N]ão? ')).upper()
    while perg not in 'SN':
        perg = str(input('RESPOSTA INVÁLIDA! [S]im ou [N]ão')).upper()
    if perg == 'N':
        break
    vendas = float(input('Valor total de vendas $: '))
    salario_total.append(200 + (vendas * 0.09))
for s in range(len(salario_total)):
    if salario_total[s] <= 299:
        c300 += 1
    elif salario_total[s] <= 399:
        c400 += 1
    elif salario_total[s] <= 499:
        c500 += 1
    elif salario_total[s] <= 599:
        c600 += 1
    elif salario_total[s] <= 699:
        c700 += 1
    elif salario_total[s] <= 799:
        c800 += 1
    elif salario_total[s] <= 899:
        c900 += 1
    elif salario_total[s] <= 999:
        c1000 += 1
    else:
        cmais += 1
print('#' * 26)
print('AMOSTRAGEM SALÁRIO'.center(26))
print('-_' * 13)
if c300 > 0:
    print(f'$200,00 - $299,00 - {c300} vendedores')
if c400 > 0:
    print(f'$299,01 - $399,00 - {c400} vendedores')
if c500 > 0:
    print(f'$399,01 - $499,00 - {c500} vendedores')
if c600 > 0:
    print(f'$499,01 - $599,00 - {c600} vendedores')
if c700 > 0:
    print(f'$599,01 - $699,00 - {c700} vendedores')
if c800 > 0:
    print(f'$699,01 - $799,00 - {c800} vendedores')
if c900 > 0:
    print(f'$799,01 - $899,00 - {c900} vendedores')
if c1000 > 0:
    print(f'$899,01 - $999,00 - {c1000} vendedores')
if cmais > 0:
    print(f'$999,01 - $****** - {cmais} vendedores')
print('*' * 26)



