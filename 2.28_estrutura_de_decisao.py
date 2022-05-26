#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                           Até 5 kg                    Acima de 5 kg
# Filé Duplo                R$ 36,00                    R$ 32,00
# Alcatra                   R$ 41,00                    R$ 37,00
# Picanha                   R$ 65,00                    R$ 59,00
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne na promoção, porém não
#há limites para a quantidade de carne por cliente. Se a compra ofr feita no cartão Tabajara o cliente receberá
#ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
#comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade carne, preço
#total, tipo de pagamento, valor do desconto e valor a pagar.

from time import sleep
tela1 = '#'*40
tela2 = '*'*40
print(tela1)
print('HIPERMERCADO TABAJARA'.center(40))
print(tela1)
print('Tipos de Corte'.center(40))
print('[F] - Filé Duplo')
print('[A] - Alcatra')
print('[P] - Picanha')
escolha = str(input('Qual carne deseja comprar? ')).upper()
kg = float(input('Quantos Kg deseja comprar? '))
tipo_pgto = str(input('Deseja pagar com cartão Tabajara? [S/N] ')).upper()
if escolha == 'F':
    tipo_carne = 'FILÉ DUPLO'
    if kg > 5:
        pc_kg = 32
    else:
        pc_kg = 36
elif escolha == 'A':
    tipo_carne = 'ALCÁTRA'
    if kg > 5:
        pc_kg = 37
    else:
        pc_kg = 41
else:
    tipo_carne = 'PICANHA'
    if kg > 5:
        pc_kg = 59
    else:
        pc_kg = 65
vl_total = pc_kg * kg
print('Emitindo Cupom Fiscal')
sleep(2)
print(tela2)
print('HIPERMERCADO TABAJARA'.center(40))
print('Cupom Fiscal'.center(40))
print(f'Tipo de carne: {tipo_carne}'.center(40))
print(f'Quantidade: {kg} Kg'.center(40))
print(f'Valor por kg: \tR${pc_kg:7.2f}'.replace('.',','))
print(f'Valot total: \tR${vl_total:7.2f}'.replace('.',','))
if tipo_pgto == 'S':
    print('Pago com Cartão Tabajara'.center(40))
    print('Você ganhou um desconto de 5%'.center(40))
    print(f'Desconto: \t\tR${vl_total * 0.05:>7.2f}'.replace('.',','))
    print(f'Valor Pago \t\tR${vl_total - vl_total * 0.05:>7.2f}'.replace('.',','))
print(tela2)
print('Obrigado pela sua compra. Volte Sempre!'.center(40))


