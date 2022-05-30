#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha
#Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50, a partir
#do preço do pão informado pelo usuário, conforme exemplo.

preco_pao = float(input('Preço do Pão: R$ '))
print('#' * 28)
print(f'PANIFICADORA PÃO DE ONTEM'.center(28))
print('-' * 28)
print(f'Tabela de Preços'.center(28))
for c in range(1, 51):
    print(f'{c:>2} - R$ {(c * preco_pao):>5.2f}'.center(28).replace('.',','))