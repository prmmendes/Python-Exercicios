#Altere o programa anterior para mostrar no final a soma dos números.

ni = int(input('Início: '))
nf = int(input('Fim: '))
s = 0
for c in range(ni, nf+1):
    print(f'{c}', end=' ')
    s = s + c
print(f'\nSoma: {s}')