#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
#limitando o fatorial a números inteiros, positivos e menores que 16.


while True:
    print('#' * 100)
    print('PROGRAMA FATORIAL'.center(100))
    print('#'*100)
    print('REGRAS - Valor mínimo = 0 | Valor máximo = 16')
    print('-' * 100)
    fatorial = int(input('Fatorial: '))
    while fatorial < 0 or fatorial > 16:
        fatorial = int(input('Digite um número válido conforme regra: '))
    aux = fatorial
    for c in range(fatorial-1, 0, -1):
        fatorial = fatorial * c
    print(f'{aux}! = {aux} x ', end='')
    for c in range(aux-1, 0, -1):
        if c > 1:
            print(f'{c} x ', end='')
        else:
            print(f'{c} = ', end='')
    print(fatorial)
    print('_' * 100)
    perg = str(input('Deseja fazer outro fatorial? [S]im ou [N]ão? ')).upper()
    while perg not in 'SN':
        perg = str(input('Responda corretamente! [S]im ou [N]ão? ')).upper()
    if perg == 'N':
        break
print('-'*100)
print('OBRIGADO POR USAR O SISTEMA!'.center(100))



