#Uma fruteira está vendendo frutas com a seguint tabela de preços:
# Morango Até 5 kg - R$ 2,50 por Kg / Acima de 5 Kg - R$ 2,20 por Kg
# Maça Até 5 kg - R$ 1,80 por Kg / Acima de 5 Kg - 1,50 por Kg
#Se o cliente compra mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
#desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
#(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

from time import sleep
tela1 = '^'*40
tela2 = '~'*40
print(tela1)
print('SACOLÃO DO PROGRAMADOR'.center(40))
print(tela2)
kg_morango = float(input('Quantidade (em Kg) de morango: '))
kg_maca = float(input('Quantidade (em Kg) de maças: '))
if kg_morango <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2
if kg_maca <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5
pt_morango = kg_morango * preco_morango
pt_maca = kg_maca * preco_maca
ptotal = pt_morango + pt_maca
kg_total = kg_morango + kg_maca
print('Emitindo demonstrativo de compra...')
print(tela2)
sleep(2)
print(f'{kg_morango} Kg de Morango')
print(f'Preço do Morango (por Kg) \tR${preco_morango:>6.2f}')
print(f'Preço total do Morango: \tR${pt_morango:>6.2f}')
print(f'{kg_maca} Kg de Maça')
print(f'Preço da Maça (por Kg) \t\tR${preco_maca:>6.2f}')
print(f'Preço total da Maça: \t\tR${pt_maca:>6.2f}')
print(f'Valor total da compra: \t\tR${ptotal:>6.2f}')
if kg_total > 8 or ptotal > 25:
    print(f'Aplicando descontos...')
    sleep(1)
    print(f'Desconto de 10% aplicado a sua compra')
    print(f'Valor final a ser pago \t\tR${ptotal*0.9:>6.2f}')
