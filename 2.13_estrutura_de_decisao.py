#Faça um programa que leia um número e exiba o dia correspondente da semana (1 - Domingo, 2 - Segunda,
#etc), se digitar outro valor deve aparecer valor inválido.

print('[1] - Domingo')
print('[2] - Segunda-Feira')
print('[3] - Terça-Feira')
print('[4] - Quarta-Feira')
print('[5] - Quinta-Feira')
print('[6] - Sexta-Feira')
print('[7] - Sábado')
dia = int(input('Digite um número para escolher o dia da semana: '))
if dia == 1:
    print('DOMINGO')
elif dia == 2:
    print('SEGUNDA-FEIRA')
elif dia == 3:
    print('TERÇA-FEIRA')
elif dia == 4:
    print('QUARTA-FEIRA')
elif dia == 5:
    print('QUINTA-FEIRA')
elif dia == 6:
    print('SEXTA-FEIRA')
elif dia == 7:
    print('SÁBADO')
else:
    print('DIA INVÁLIDO')