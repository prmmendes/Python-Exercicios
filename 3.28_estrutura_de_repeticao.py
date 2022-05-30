#Faça um programa que calcule o valor investido por um colecionador em sua coleção de CD's e o valor
#médio gasto em cada um deles. O usuário deve informar a quantidade de CD's e o valor de cada um.

colecao = int(input('Quantos CDs há na coleção? '))
s_preco = 0
for c in range(1, colecao + 1):
    preco = float(input(f'Valor do CD {c}: '))
    s_preco += preco
print(f'Quantidade: {colecao} CDs na Coleção')
print(f'Total em R$ {s_preco:6.2f}')
print(f'Media em R$ {(s_preco / colecao):6.2f}')
