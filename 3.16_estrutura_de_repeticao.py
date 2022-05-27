#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,...
#Faça um programa que gere a série até que o valor seja maior que 500.

a = 1
b = 1
fibonacci = a + b
cont = 0
while True:
    if cont == 0:
        print(a, b, end=' ')
    else:
        fibonacci = a + b
        a = b
        b = fibonacci
        print(fibonacci, end=' ')
    cont += 1
    if fibonacci > 500:
        break


