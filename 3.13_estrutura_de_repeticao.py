#Faça um programa que peça dois números, base e expoente e mostre o primeiro número elevado ao segundo
#número. Não utilize a função de potência da linguagem.

print('POTÊNCIA'.center(16))
print('-'*16)
base = int(input('Base: '))
expoente = int(input('Expoente: '))
resultado = 1
print('-'*16)
if base == 0:
    resultado = 0
elif expoente == 1:
    resultado = 1
else:
    for c in range(0, expoente):
        resultado = resultado * base
print(f'{base}^{expoente} = {resultado}')
