#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
#area a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
#que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de
#latas de tinta a serem compradas e o preço total.

from math import ceil

area = float(input('Area a ser pintada em m²: '))
tinta = area / 3
cons = ceil(tinta / 18)
print(f'Para a pintura de {area}m² serão necessários {tinta:.1f} litros')
print(f'Portanto comprando {cons} lata(s) de tinta você conseguirá pintar toda a área informada')
print(f'Valor total de R${cons*80:.2f}')


