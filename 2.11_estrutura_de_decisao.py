#As organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
#para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um
#colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5%
#Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste.
# o percentual de aumento aplicado.
# o valor do aumento;
# o novo salário, após o aumento.

sal = float(input('Salário: R$'))
if sal <= 280:
    reajuste = sal * 0.2
    percentual = 20
elif sal > 280 and sal < 700:
    reajuste = sal * 0.15
    percentual = 15
elif sal >= 700 and sal < 1500:
    reajuste = sal * 0.1
    percentual = 10
else:
    reajuste = sal * 0.05
    percentual = 5
print('_-'*20)
print('TABELA DE REAJUSTE SALARIAL'.center(40))
print('_-'*20)
print(f'Salário Atual: \t\tR${sal:.2f}')
print(f'% de Aumento: \t\t{percentual}%')
print(f'Valor Reajuste: \tR${reajuste:.2f}')
print(f'Novo Salário: \t\tR${sal + reajuste:.2f}')
print('_-'*20)