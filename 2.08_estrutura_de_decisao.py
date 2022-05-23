#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Produto A - \tR$'))
p2 = float(input('Produto B - \tR$'))
p3 = float(input('Produto C - \tR$'))
mb = 0
if p1 <= p2 and p1 <= p3:
    mb = p1
elif p2 <= p3 and p2 <= p1:
    mb = p2
else:
    mb = p3
print(f'Melhor preço - \tR${mb:.2f}')