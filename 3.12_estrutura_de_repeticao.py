#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10.
#O usuário deve informar qualquer número que deseja ver a tabuada.

from time import sleep
numero = int(input('Imprimir tabuada (1 a 10) de: '))
while numero < 0 or numero > 10:
    numero = int(input('Erro! Digite um valor Válido: ' ))
print(f'Gerando Tabuada de {numero}')
sleep(1.5)
print('#'*20)
print(f'TABUADA DE {numero}'.center(20))
print('-'*20)
for i in range(1, 11):
    print(f'{numero:>2} X {i:>2} = {numero*i:>2}'.center(20))
print('#'*20)