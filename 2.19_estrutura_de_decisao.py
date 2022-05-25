#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas,
# e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros.

numero = int(input('Digite um número inteiro maior que 0 e menor que 1000: '))
unidade = (numero // 1) % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10

if numero > 0 and numero < 1000:
    if numero > 99:
        if unidade == 0 or unidade == 1:
            textu = 'unidade'
        else:
            textu = 'unidades'
        if dezena == 0 or dezena == 1:
            textd = 'dezena'
        else:
            textd = 'dezenas'
        if centena == 0 or centena == 1:
            textc = 'centena'
        else:
            textc = 'centenas'
        if centena == 0 and dezena == 0 and unidade > 0:
            print(f'{unidade} {textu}')
        elif centena == 0 and dezena > 0 and unidade == 0:
            print(f'{dezena} {textd}')
        elif centena == 0 and dezena > 0 and unidade > 0:
            print(f'{dezena} {textd} e {unidade} {textu}')
        elif centena > 0 and dezena == 0 and unidade > 0:
            print(f'{centena} {textc} e {unidade} {textu}')
        elif centena > 0 and dezena > 0 and unidade == 0:
            print(f'{centena} {textc} e {dezena} {textd}')
        elif centena > 0 and dezena == 0 and unidade == 0:
            print(f'{centena} {textc}')
        else:
            print(f'{centena} {textc}, {dezena} {textd} e {unidade} {textu}')
    elif numero > 9:
        if dezena == 0 or dezena == 1:
            textd = 'dezena'
        else:
            textd = 'dezenas'
        if unidade == 0 or unidade == 1:
            textu = 'unidade'
        else:
            textu = 'unidades'
        if dezena == 0 and unidade > 0:
            print(f'{unidade} {textu}')
        elif dezena > 0 and unidade == 0:
            print(f'{dezena} {textd}')
        else:
            print(f'{dezena} {textd} e {unidade} {textu} ')
    else:
        if unidade == 0 or unidade == 1:
            textu = 'unidade'
        else:
            textu = 'unidades'
        print(f'{unidade} {textu}')
else:
    print(f'{numero} - Número inválido!')







