#Sendo H = 1 + 1/2 + 1/3 + 3/5 + 4/7 + 5/9 + n/m. Imprima no final a soma da série

termos = int(input('Quantos termos deseja calcular: '))
a = 1
b = 1
sa = 1
sb = 1
print(f'{a}/{b}', end=' ')
for c in range (1, termos):
    a += 1
    b += 2
    print(f'+ {a}/{b}', end=' ')
    sa += a
    sb += b
print(f' = {sa}/{sb}')

