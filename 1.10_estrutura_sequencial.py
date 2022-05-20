#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

tpc = float(input('Temperatura em ºC: '))
tpf = tpc * 1.8 + 32
print(f'{tpc}ºC = {tpf}ºF')