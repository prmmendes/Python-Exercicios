#As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado
#durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como um projeção de quanto
#será gasto com pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os repre-
#sentantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
#Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; O píso do abono será de R$ 300,00,
#isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se dever ter
#nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu pro-7
#grama deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário
#igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono con-
#cedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# a) O salário de cada funcionário, juntamente com o valor do abono
# b) O número total de funcionários processados
# c) O valor total a ser gasto com o pagamento do abono
# d) O número de funcionários que receberão o valor mínimo de 300 reais
# e) O maior valor pago como abono.

salarios = []
abonos = []
cont = abono_min = 0
while True:
    salario = float(input('Salário: R$ '))
    if salario == 0:
        break
    salarios.append(salario)
    if salario * 0.2 < 300:
        abonos.append(300.00)
        abono_min += 1
    else:
        abonos.append(salario*0.2)
    cont += 1
for s in range(len(salarios)):
    print(f'Salário R$ {salarios[s]:>8.2f} - Abono R$ {abonos[s]:>8.2f}')
print(f'Foram processados {cont} Colaboradores')
print(f'Serão gastos R${sum(abonos):>8.2f} com Abonos')
print(F'O valor mínimo do Abono será pago a {abono_min} Colaboradores')
print(f'O maior valor de abono pago será de R$ {max(abonos):>8.2f}')