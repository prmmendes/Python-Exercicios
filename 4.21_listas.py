#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
#Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com
#um litro de combustível. Calcule e mostre:
# a) O modelo do carro mais ecônomico
# b) Quantos litros de Combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilô-
#metros e quanto isto custará, considerando o valor da Gasolina.

carros = []
consumo = []
for c in range(5):
    print(f'Veículo {c+1}')
    carros.append(str(input('Modelo: ')))
    consumo.append(float(input('Km/l: ')))
menor_consumo = consumo.index(max(consumo))
print('^~v' * 15)
print('RELATÓRIO FINAL'.center(45))
print('^~v' * 15)
for c in range(5):
    print(f'{c+1} - {carros[c]} - {consumo[c]} Km/lts  - Em 1000 Km --> {1000/consumo[c]:>6.2f}lts - Custo Total: R$ {(1000/consumo[c])*7.59:>8.2f}')
print(f'O menor consumo é do {carros[menor_consumo]}')