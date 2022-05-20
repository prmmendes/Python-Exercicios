#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

vr_h = float(input('Valor Hora - R$'))
hr_t = int(input('Horas Trabalhadas: '))
print(f'Salário Total: R${vr_h * hr_t:.2f}')