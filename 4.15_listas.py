#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
#de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
# a) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# b) Exiba todos os valores na ordem inversa
# c) Calcule e mostre a soma dos valores;
# d) Calcule e mostre a média dos valores;
# e) Calcule e mostre a quantidade de valores acima da média calculada;
# f) Calcule e mostre a quantidade de valores abaixo de sete;
# g) Encerre o programa com uma mensagem;

notas = []
cont = 0
while True:
    cont += 1
    nota = float(input(f'Digite a {cont}ª Nota: (-1 para SAIR:) '))
    while nota < -1 or nota > 10:
        nota = float(input('NOTA INVÁLIDA! Digite uma nota de [0] a [10]: (-1 para SAIR:) '))
    if nota == -1:
        break
    notas.append(nota)
print('#' * 30)
print('Notas Lançadas: ', end='')
for n in notas:
    print(n, end=' | ')
print()
print('Notas Lançadas (Invertidas): ', end='')
notas_invertidas = notas.reverse()
for i in notas:
    print(i, end=' | ')
print()
print('-' * 50)
soma = sum(notas)
media = soma/len(notas)
contm = 0
conta = 0
for c in range(len(notas)):
    if notas[c] > media:
        contm += 1
    if notas[c] < 7:
        conta += 1
print(f'Soma da Notas Lançadas   --> {soma}')
print(f'Média das Notas Lançadas --> {media:.2f}')
print(f'{contm} notas estão acima da média')
print(f'{conta} notas estão abaixo de 7')
print('#' * 50)
print(f'OBRIGADO POR USAR O SISTEMA!')