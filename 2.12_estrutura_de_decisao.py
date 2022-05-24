#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de
#Renda, que depende do salário bruno (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
#a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O salário liquido corresponde
#ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de
#horas trabalhadas no mês.
# Desconto do IR:
# até 900 (inclusive) - isento
# até 1500 (inclusive) - desconto de 5%
# até 2500 (inclusive) - desconto de 10%
# acima de 2500 - desconto de 20%
#Imprima na tela todas as informações

valorh = float(input('Valor da Hora: '))
horast = int(input('Quantidade de horas trabalhadas: '))
salariob = valorh * horast
sindicato = salariob * 0.03
inss = salariob * 0.1
fgts = salariob * 0.11
ir = 0
if salariob <= 900:
    perc = 'Isento'
elif salariob <= 1500:
    perc = '5%'
    ir = salariob * 0.05
elif salariob <= 2500:
    perc = '10%'
    ir = salariob * 0.1
else:
    perc = '20%'
    ir = salariob * 0.2
totaldes =  sindicato + inss + ir
salariol = salariob - totaldes
print('+-'*25)
print('FOLHA DE PAGAMENTO'.center(50))
print('-+'*25)
print(f'Salário Bruto: R${valorh:.2f} x {horast}h\t\tR${salariob:>8.2f}'.replace('.',','))
print(f'(-) IRRF ({perc}) \t\t\t\t\t\tR${ir:>8.2f}'.replace('.',','))
print(f'(-) INSS (10%) \t\t\t\t\t\tR${inss:>8.2f}'.replace('.',','))
print(f'(-) Sindicato (3%) \t\t\t\t\tR${sindicato:>8.2f}'.replace('.',','))
print(f'FGTS (11%) \t\t\t\t\t\t\tR${fgts:>8.2f}'.replace('.',','))
print(f'Total de descontos: \t\t\t\tR${totaldes:>8.2f}'.replace('.',','))
print(f'Salário Líquido: \t\t\t\t\tR${salariol:>8.2f}'.replace('.',','))
print('+-'*25)
