#Faça um programa  que peça um data no formato dd/mm/aaaa e determine se a mesma é uma data válida

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia > 0 and dia <= 31):
    print('DATA VÁLIDA')
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia > 0 and dia <= 30):
    print('DATA VÁLIDA')
elif (mes == 2) and (dia > 0 and dia <= 28):
    print('DATA VÁLIDA')
elif (ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0) and dia == 29:
    print('DATA VÁLIDA')
else:
    print('DATA INVÁLIDA')

