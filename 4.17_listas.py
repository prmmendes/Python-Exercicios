#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será deter-
#minado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
#alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser
#encerrado quando não for informado o nome do atleta. A saída do Programa deve ser conforme o exemplo abaixo:

saltos = []
ordem_salto = ('Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto')
atleta = ' '
while True:
    atleta = str(input('Atleta: '))
    if atleta == '':
        break
    for s in range(5):
        saltos.append(float(input(f'{ordem_salto[s]} Salto: ')))
    print('^~v'*15)
    print('RESULTADO FINAL'.center(45))
    print('^~v'*15)
    print(f'Atleta: {atleta}')
    print(f'Saltos: ', end='')
    for i,c in enumerate(saltos):
        if i < 4:
            print(f'{c}m - ', end=' ')
        else:
            print(f'{c}m')
    print(f'Média dos saltos: {sum(saltos)/5:.2f}m')
    saltos.clear()
