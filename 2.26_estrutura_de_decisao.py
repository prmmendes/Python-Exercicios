#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a) Alccol - Até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro
# b) Gasolina - até 20 litros, desconto de 4% por litro. Acima de 20 litros, desconto de 6% por litro.
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte
#forma: A - alcool, G - Gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo que o preço
#do litro da gasolina é R$ 7,50 e o preço do alcool é R$ 5,90

from time import sleep
tela = '*' * 45
print(tela)
print('POSTO PAULÃO'.center(45))
print(tela)
print('[G] - GASOLINA')
print('[A] - ÁLCOOL')
tipo = str(input('Escolha o tipo de Abastecimento: ')).upper()
qte = float(input('Quantidade em lts: '))
if tipo == 'A':
    if qte > 20:
        print('Abastecendo...')
        sleep(2)
        print(tela)
        print(f'Tipo de Combustível: ÁLCOOL ')
        print(f'Quantidade - {qte} Litros')
        print(f'Valor por litro: \t R$ 5,90')
        print(f'Valor Total: \t R$ {5.9 * qte:>7.2f}')
        print(f'Desconto com desconto de 5%')
        print(f'Valor Total: \t R$ {(5.9 * qte)*0.95:>7.2f}')
    else:
        print('Abastecendo...')
        sleep(2)
        print(tela)
        print(f'Tipo de Combustível: ÁLCOOL ')
        print(f'Quantidade - {qte} Litros')
        print(f'Valor por litro: \t R$ 5,90')
        print(f'Valor Total: \t R$ {5.9 * qte:>7.2f}')
        print(f'Desconto com desconto de 3%')
        print(f'Valor Total: \t R$ {(5.9 * qte) * 0.97:>7.2f}')
else:
    if qte > 20:
        print('Abastecendo...')
        sleep(2)
        print(tela)
        print(f'Tipo de Combustível: GASOLINA ')
        print(f'Quantidade - {qte} Litros')
        print(f'Valor por litro: \t R$ 7,50')
        print(f'Valor Total: \t R$ {7.5 * qte:>7.2f}')
        print(f'Desconto com desconto de 6%')
        print(f'Valor Total: \t R$ {(7.5 * qte)*0.94:>7.2f}')
    else:
        print('Abastecendo...')
        sleep(2)
        print(tela)
        print(f'Tipo de Combustível: GASOLINA ')
        print(f'Quantidade - {qte} Litros')
        print(f'Valor por litro: \t R$ 7,50')
        print(f'Valor Total: \t R$ {7.5 * qte:>7.2f}')
        print(f'Desconto com desconto de 4%')
        print(f'Valor Total: \t R$ {(7.5 * qte) * 0.96:>7.2f}')