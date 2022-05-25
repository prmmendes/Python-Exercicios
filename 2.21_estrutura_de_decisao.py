#Faça um programa para um caixa eletrônico. O Programa deverá perguntar ao usuário o valor do saque e
#depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as 1, 5, 10,
#50, e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não dever se preocupar
#com a quantidade de notas existentes na máquina.

from time import sleep
tela = '#'*40
n100 = n50 = n10 = n5 = n1 = 0
print(tela)
print('CAIXA ELETRÔNICO BPR'.center(40))
print(tela)
print('Valor mínimo: R$  10,00')
print('Valor maxímo: R$ 600,00')
saque = int(input('Valor do Saque: '))
print('-'*40)
print('Aguarde, emitindo saque...')
sleep(2)
print('-'*40)
if saque >= 10 and saque <= 600:
    rest = saque
    if rest >= 100:
        n100 = rest // 100
        rest = rest % 100
    if rest > 0:
        n50 = rest // 50
        rest = rest % 50
    if rest > 0:
        n10 = rest // 10
        rest = rest % 10
    if rest > 0:
        n5 = rest // 5
        rest = rest % 5
    if rest > 0:
        n1 = rest // 1
    print(f'Saque: R$ {saque}')
    if n100 > 0:
        print(f'[{n100}] nota(s) de R${100.00:>7.2f}'.replace('.',','))
    if n50 > 0:
        print(f'[{n50}] nota(s) de R${50.00:>7.2f}'.replace('.',','))
    if n10 > 0:
        print(f'[{n10}] nota(s) de R${10.00:>7.2f}'.replace('.',','))
    if n5 > 0:
        print(f'[{n5}] nota(s) de R${5.00:>7.2f}'.replace('.',','))
    if n1 > 0:
        print(f'[{n1}] nota(s) de R${1.00:7.2f}'.replace('.',','))
elif saque < 10:
    print(f'Impossível sacar - R${saque} | Valor mínimo - R$ 10,00')
else:
    print(f'Impossível sacar - R${saque} | Valor máximo - R$ 600,00')

