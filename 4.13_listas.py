#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

from time import sleep
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
temperaturas = []
for m in range(12):
    temperaturas.append(float(input(f'Média de Temperaturas no mês {meses[m]}: ')))
media_anual = sum(temperaturas)/12
print(f'Média Anual de Temperaturas: {media_anual:.2f}ºC')
print(f'Meses com Temperatura acima da Média'.center(36))
sleep(1.5)
print('#' * 36)
for t in range(12):
    if temperaturas[t] > media_anual:
        print(f'Mês: {meses[t]} \t| Temperatura: {temperaturas[t]}')
        print('-' * 36)
        sleep(1.5)