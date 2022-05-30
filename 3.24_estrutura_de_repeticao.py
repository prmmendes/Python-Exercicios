#Faça um programa que calcule e mostre a média aritmética de N notas.

soma = cont = 0
while True:
    nota = float(input('Digite uma nota: '))
    soma += nota
    cont += 1
    perg = str(input('Deseja lançar nova Nota? [S]im ou [N]ão? ')).upper()
    while perg not in 'SN':
        perg = str(input('Resposta Inválida! Deseja lançar nova Nota? [S]im ou [N]ão?  ')).upper()
    if perg == 'N':
        break
print(f'Foram lançados {cont} Notas. ')
print(f'A soma das notas lançadas é: {soma}')
print(f'A média das Notas lançadas é: {soma/cont}')
