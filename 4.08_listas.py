#Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []
for p in range(5):
    print(f'{p+1}ª Pessoa'.center(15))
    idades.append(int(input('Idade: ')))
    alturas.append(float(input('Altura: ')))
    print('-' * 15)
idades_inv = idades[::-1]
alturas_inv = alturas[::-1]
print('ORDEM DE CORRETA')
print(f'Idades: {idades}')
print(f'Alturas: {alturas}')
print('-' * 15)
print('ORDEM INVERSA')
print(f'Idades: {idades_inv}')
print(f'Alturas: {alturas_inv}')

