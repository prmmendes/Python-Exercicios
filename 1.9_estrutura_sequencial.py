#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em
# graus Celsius. C = 5 * ((F-32) / 9).

tpf = float(input('Digite a Temperatura em ºF: '))
tpc = 5 * ((tpf - 32) / 9)
print(f'{tpf}ºF = {tpc}ºC')