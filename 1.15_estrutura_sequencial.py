#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

vr_h = float(input('Valor da hora/trabalho: '))
hr_m = int(input('Horas trabalhadas no mês: '))
sal_b = vr_h * hr_m
ir = sal_b * 0.11
inss = sal_b * 0.08
sind = sal_b * 0.05
sal_l = sal_b - ir - inss - sind

print('-*'*15)
print(f'Salário Bruto -\t\tR${sal_b:.2f}')
print(f'Imposto de Renda -\tR${ir:.2f}')
print(f'INSS -\t\t\t\tR${inss:.2f}')
print(f'Sindicato -\t\t\tR${sind:.2f}')
print('*-'*15)
print(f'Salário Líquido -\tR${sal_l:.2f} ')