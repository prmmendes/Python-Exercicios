#O Cardápio de uma Lanchonete é o seguinte
#   Especificação           Código              Preço
#   Cachorro Quente         100                 R$  8,00
#   Bauru Simples           101                 R$  9,00
#   Bauru com Ovo           102                 R$ 10,50
#   Hamburguer              103                 R$ 12,30
#   Cheeseburguer           104                 R$ 13,00
#   Refrigerante            105                 R$  5,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a
#ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente de informar quando
#o pedido deve ser encerrado.

from time import sleep
cachorro_q = 0
bauru_s = 0
bauru_c = 0
hamburguer = 0
cheese = 0
refrigerante = 0
tela1 = '#' * 60
tela2 = '_-' * 30
tela3 = '-' * 60
print(tela1)
print('LANCHONETE MEQUIDONALDS'.center(60))
print(tela1)
print('Especificação           Código              Preço')
print(tela2)
print('Cachorro Quente           100               R$  8,00')
print('Bauru Simples             101               R$  9,00')
print('Bauru com Ovo             102               R$ 10,50')
print('Hamburguer                103               R$ 12,30')
print('Cheeseburguer             104               R$ 13,00')
print('Refrigerante              105               R$  5,00')
print(tela2)
while True:
    cod_pedido = int(input('Código do Pedido: [0] para Encerrar Pedido: '))
    if cod_pedido == 0:
        break
    if cod_pedido < 100 or cod_pedido > 105:
        cod_pedido = int(input('Pedido Inválido! Consulte Cardápio e digite o Código Correto: '))
    if cod_pedido == 100:
        cachorro_q += 1
    elif cod_pedido == 101:
        bauru_s += 1
    elif cod_pedido == 102:
        bauru_c += 1
    elif cod_pedido == 103:
        hamburguer += 1
    elif cod_pedido == 104:
        cheese += 1
    else:
        refrigerante +=1
total_cachorro = cachorro_q * 8
total_bauru_s = bauru_s * 9
total_bauru_c = bauru_c * 10.5
total_hamburguer = hamburguer * 12.3
total_chesse = cheese * 13
total_refri = refrigerante * 5
total_geral = total_cachorro + total_bauru_s + total_bauru_c + total_hamburguer + total_chesse + total_refri
print('Aguarde! Emitindo Nota Fiscal...'.center(60))
sleep(3)
print(tela1)
print('NOTA FISCAL ELETRÔNICA'.center(60))
print(tela2)
if cachorro_q > 0:
    print(f'{cachorro_q}x Cachorro Quente  \tR${total_cachorro:>6.2f}')
if bauru_s > 0:
    print(f'{bauru_s}x Bauru Simples  \t\tR${total_bauru_s:>6.2f}')
if bauru_c > 0:
    print(f'{bauru_c}x Bauru com Ovo \t\tR${total_bauru_c:>6.2f}')
if hamburguer > 0:
    print(f'{hamburguer}x Hamburguer \t\t\tR${total_hamburguer:>6.2f}')
if cheese > 0:
    print(f'{cheese}x Cheeseburguer \t\tR${total_chesse:>6.2f} ')
if refrigerante > 0:
    print(f'{refrigerante}x Refrigerante \t\tR${total_refri:>6.2f}')
print(tela3)
print(f'Total das Compras \t\tR${total_geral:>6.2f}')
print(tela2)
print('OBRIGADO! BOM APETITE!'.center(60))




