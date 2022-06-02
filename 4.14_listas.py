#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
# a) "Telefonou para a vítima?"
# b) "Esteve no local do crime?"
# c) "Mora perto da vítima?"
# d) "Devia para a vítima?"
# e) "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
#positivamente a 2 questões ela deve ser classificada como "Suspeita", #entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ('Telefonou para a Vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?',
             'Devia para a vítima?', 'Já trabalhou com a vítima?')
respostas = []
for p in range(5):
    print(f'Pergunta {p+1} \n{perguntas[p]}')
    resp = str(input('Responda [S]im ou [N]ão: ')).upper()
    while resp not in 'SN':
        resp = str(input(f'RESPOSTA INVÁLIDA | Responda [S]im ou [N]ão: ')).upper()
    if resp == 'S':
        respostas.append(1)
    else:
        respostas.append(0)
    print('-_' * 20)
if sum(respostas) == 2:
    print('Você é SUSPEITO!')
elif sum(respostas) == 3 or sum(respostas) == 4:
    print(f'Você é CÚMPLICE!')
elif sum(respostas) == 5:
    print(f'Você é ASSASSINO!')
else:
    print(f'Você é INOCENTE!')