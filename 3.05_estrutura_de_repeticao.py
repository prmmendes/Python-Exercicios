#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

from time import sleep
cont = 0
ano = int(input('Ano de Início da Análise: '))
a = int(input('Digite a População do País A: '))
while a <= 0:
    a = int(input('População digitada menor ou igual a 0. Digite novamente: '))
txa = float(input('Digite a taxa (%) de crescimento de A: '))/100
b = int(input('Digite a População do País B: '))
while b <= 0:
    b = int(input('População digitada menor ou igual a 0. Digite novamente: '))
txb = float(input('Digite a taxa (%) de crescimento de B: '))/100
an = a
bn = b
while an < bn:
    an = an + (an * txa)
    bn = bn + (bn * txb)
    cont += 1
print('*'* 45)
print('CALCULANDO TAXAS DEMOGRÁFICAS'.center(45))
print('*'* 45)
print(f'Ano inicial de Análise: {ano}')
print(f'População de A: {a:>8} habitantes', end=' | ')
print(f'Taxa de crescimento: {txa*100:>4.2}%')
print(f'População de B: {b:>8} habitantes', end=' | ')
print(f'Taxa de crescimento: {txb*100:>4.2}')
if a >= b:
    print('A população de A é igual ou maior que B')
else:
    print('*'*45)
    print(f'No ano {ano + cont} A será maior que B')
    print(f'Nova população de A: {an.__ceil__():>7} habitantes')
    print(f'Nova população de B: {bn.__ceil__():>7} habitantes')
    print(f'Serão necessários {cont} anos')



