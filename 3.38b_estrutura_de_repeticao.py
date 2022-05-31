#Após concluir o exercício anterior, altere o programa permitindo que o usuário digite o salário
#inicial do funcionário

from datetime import date
salario_inicial = float(input('Salário: '))
reajuste = 0.015
salario_atualizado = salario_inicial + (salario_inicial * 0.015)
ano_atual = date.today().year
reajuste = reajuste * 2 
for a in range(1997, ano_atual+1):
    salario_atualizado = salario_atualizado + (salario_atualizado * reajuste)
    print(f'Ano: {a} | Reajuste {reajuste}% | Salário: R${salario_atualizado:.2f}')