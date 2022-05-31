#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# a) valor da dívida
# b) valor dos juros
# c) quantidade de parcelas
# d) valor da parcela
#Os juros e a quantidade de parcelas seguem:
# Qte de Parc.         % de Juros
#       1                   0
#       3                   10
#       6                   15
#       9                   20
#       12                  25

while True:
    divida = float(input('Dívida - R$ [0] para Sair: '))
    if divida == 0:
        break
    parcelas = int(input('Quantidade de Parcelas: '))
    if parcelas < 3:
        juros = 0.0
    elif parcelas >= 3 and parcelas < 6:
        juros = 0.1
    elif parcelas >= 6 and parcelas < 9:
        juros = 0.2
    else:
        juros = 0.25
    print('#' * 40)
    print('RESUMO DA DÍVIDA'.center(40))
    print('-' * 40)
    print(f'Valor da Dívida: \t\tR${divida:>8.2f}'.replace('.',','))
    print(f'Juros:           \t\t{juros*100}%')
    print(f'Valor dos Juros: \t\tR${divida*juros:>8.2f}'.replace('.',','))
    print(f'Valor Total:     \t\tR${divida + divida*juros:>8.2f}'.replace('.',','))
    print(f'Nº de Parcelas:  \t\t{parcelas}')
    print(f'Valor Parcelas:  \t\tR${(divida + (divida*juros)) / parcelas:>8.2f}')
    print('-' * 40)
print('Obrigado por usar o Sistema!')

