#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#Telefonou para a vítima?"
#Esteve no local do crime?"
#Mora perto da vítima?"
#Devia para a vítima?"
#Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

from time import sleep
tela = '#' * 60
soma = 0
print(tela)
print('SOFTWARE DETETIVE'.center(60))
print(tela)
print('Responda as perguntas que seguem com [S] or [N]')
telefone = str(input('Telefonou para a vítima? ')).lower()
local = str(input('Esteve no local do crime? ')).lower()
mora = str(input('Mora perto da vítima? ')).lower()
debito = str(input('Devia para a vítima? ')).lower()
trabalho = str(input('Trabalhava com a vitíma? ')).lower()
if telefone == 's':
    soma += 1
if local == 's':
    soma += 1
if mora == 's':
    soma += 1
if debito == 's':
    soma += 1
if trabalho == 's':
    soma += 1
print(tela)
print('Analisando Respostas...')
sleep(2)
print(tela)
if soma == 2:
    print('VOCÊ É SUSPEITO!')
elif soma == 3 or soma == 4:
    print('VOCÊ É CÚMPLICE!')
elif soma == 5:
    print('VOCÊ É O ASSASSINO!')
else:
    print('VOCÊ É INOCENTE!')



