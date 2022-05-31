#Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
# a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00
# b) Em 1996 recebeu aumento de de 1,5% sobre seu salário inicial
# c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano
#anterior. Faça um programa que determine o salário atual desse funcionário.

from datetime import date

salario_inicial = 1000
reajuste = 0.015
salario_atualizado = salario_inicial + (salario_inicial * 0.015)
ano_atual = date.today().year
reajuste = reajuste * 2
for a in range(1997, ano_atual+1):
    salario_atualizado = salario_atualizado + (salario_atualizado * reajuste)
    print(f'Ano: {a} | Reajuste {reajuste}% | Salário: R${salario_atualizado:.2f}')