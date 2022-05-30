#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
#informados também pelo usuário, conforme exemplo.

numero = int(input('Digite um número inteiro para gerar tabuada: '))
inicio = int(input('Iniciar tabuada no termo: '))
fim = int(input('Finalizar tabuada no termo: '))
print('#' * 40)
print(f'TABUADA DE: {numero}'.center(40))
print('#' * 40)
print(f'Vou montar a tabuada de {numero}, \ncomeçando em {inicio} e terminando em {fim}'.center(40))
for t in range(inicio, fim + 1):
    print(f'{numero} x {t} = {numero * t}'.center(40))