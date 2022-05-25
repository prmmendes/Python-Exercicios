#Faça um programa para leitura de três notas parciais de uma aluno. O programa deve calcular a média
#alcançada por um aluno e apresentar:
# a) a mensagem 'Aprovado', se a média for maior ou igual a 7, com a respectiva média alcançada
# b) a mensagem 'Reprovado', se a média for menor do que 7, com a respectiva média alcançada
# c) a mensagem 'Aprovado com Distinção', se a média for igual a 10

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3) / 3
if media < 0 and media > 10:
    print('Confira as notas lançadas!')
elif media == 10:
    print(f'Média - {media}  | APROVADO COM DISTINÇÃO')
elif media >= 7:
    print(f'Média - {media}  | APROVADO')
else:
    print(f'Média - {media}  | REPROVADO')