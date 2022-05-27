#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n-ésimo termo.

termos = int(input('Quantos termos da sequência de Fibonacci quer gerar? '))
fibonacci = 0
a = 0
b = 1
fibonacci = 0
for n in range(0, termos):
    if n == 0:
        print(a, end=' ')
    else:
        fibonacci = b + a
        a = b
        b = fibonacci
        print(fibonacci, end=' ')

