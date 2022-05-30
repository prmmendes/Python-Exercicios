#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número
#primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programaque peça um número inteiro
#e determine se le é ou não um número primo.

numero = int(input('Digite um número para verificar se é primo: '))
cont = 0
aux = numero
while aux >= 1:
    rest = numero % aux
    if rest == 0:
        cont += 1
    aux -= 1
if cont <= 2:
    print(f'O número {numero} É PRIMO!')
else:
    print(f'O número {numero} NÃO É PRIMO!')