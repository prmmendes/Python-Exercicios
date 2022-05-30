#Altere o programa de cálculo dos números primos, informando caso o número não seja primo, por quais
#números ele é divisível.

numero = int(input('Digite o número para verificar se é primo? '))
cont = 0
aux = numero
while aux >= 1:
    rest = numero % aux
    if rest == 0:
        print(f'O número {numero} é divisível por {aux}')
        cont += 1
    aux -= 1
if cont > 2:
    print(f'Portanto o número {numero} NÃO É PRIMO!')
else:
    print(f'Portanto o número {numero} É PRIMO!')

