#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input('Verificar números primos entre 1 e ? | [Digite um número para construir intervalo]: '))
contp = 0
for c in range(1, numero+1):
    aux = c
    cont = 0
    while aux >= 1:
        rest = c % aux
        if rest == 0:
            cont += 1
        aux -= 1
    if cont <= 2:
        print(f'O número {c} é PRIMO!')
        contp += 1
print(f'Entre o número [1] até o [{numero}] existem {contp} números primos')

