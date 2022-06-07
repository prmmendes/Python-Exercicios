#Faça um Programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
#Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1-6) e uma função para
#gerar números aleatórios, simulando os lançamentos dos dados.

from random import randint
valor_dados = [0, 0, 0, 0, 0, 0]
for d in range(100):
    dado = randint(1, 6)
    valor_dados[dado - 1] += 1
print('-='* 17)
print('RELATÓRIO FINAL DE SAÍDA DO DADO'.center(34))
print('=-'* 17)
print('Número   Quantidade  Percentual')
for c in range(6):
    print(f'{c+1}\t\t\t {valor_dados[c]}\t\t\t{valor_dados[c]:>.1f}%')