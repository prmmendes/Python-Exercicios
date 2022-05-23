#Faça um programa para um loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
#a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
#tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações
# 1) comprar apenas latas de 18 litros
# 2) comprar apenas galões de 3,6 litros
# 3) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga, e
#sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil
from math import floor

print('*'*50)
area = float(input('Area a ser pintada em m²: '))
print('*'*50)
tinta = (area / 6) * 1.1
latao = ceil(tinta / 18)
latin = ceil(tinta / 3.6)
minlatao = floor(tinta / 18)
rest = tinta - (minlatao * 18)
minlatin = ceil(rest / 3.6)
print(f'Total da área: \t\t\t\t\t{area}m²')
print(f'Qte de tinta + 10% : \t\t\t{tinta:.1f} litros')
print(f'Qte de latas de 18 litros: \t\t{latao} lata(s)')
print(f'Valor da Compra: \t\t\t\tR${latao*80:.2f}')
print(f'Desperdício de tinta em litros: {(latao * 18 - tinta):.1f} litros')
print('='*50)
print(f'Total da área: \t\t\t\t\t{area}m²')
print(f'Qte de tinta + 10% : \t\t\t{tinta:.1f} litros')
print(f'Qte de latas de 3,6 litros: \t{latin} lata(s)')
print(f'Valor da Compra: \t\t\t\tR${latin*25:.2f}')
print(f'Desperdício de tinta em litros: {(latin * 3.6) - tinta:.1f} litros')
print('='*50)
print(f'Total da área: \t\t\t\t\t{area}m²')
print(f'Qte de tinta + 10% : \t\t\t{tinta:.1f} litros')
print(f'Qte de latas de 18 litros: \t\t{minlatao} lata(s)')
print(f'Qte de latas de 3.6 litros: \t{minlatin} latas(s)')
print(f'Valor da Compra: \t\t\t\tR${(minlatao * 80) + (minlatin * 25):.2f}')
print(f'Desperdício de tinta em litros: {(minlatao * 18) + (minlatin * 3.6) - tinta:.1f} litros')

