#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista de números primos existentes
#entre 1 e um número inteiro informado pelo usuário.

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
        print(f'O número {c:>3} é PRIMO!')
        contp += 1
print(f'Entre o número [1] até o [{numero}] existem {contp} números primos')

