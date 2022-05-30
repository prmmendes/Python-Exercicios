#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar
#o cálculo de quanto cada cliente dever pagar ele desenvolveu uma tabela que contém o número de itens que
#o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar
#quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o
#programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo.

print('#' * 28)
print(f'LOJAS QUASE DOIS'.center(28))
print('-' * 28)
print(f'Tabela de Preços'.center(28))
for c in range(1, 51):
    print(f'{c:>2} - R$ {(c * 1.99):6.2f}'.center(28).replace('.',','))