#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
#alcançada pelo aluno e apresentar:
# A mensagem aprovado, se a média alcançada for maior ou igual a sete;
# A mensagem reprovado, se a média for menor do que sete
# A mensagem aprovado com distinção, for igual a dez.

n1 = float(input('Digite 1ª Nota: '))
n2 = float(input('Digite 2ª Nota: '))
med = (n1 + n2) / 2
if med == 10:
    print(f'Média: \t{med} pontos')
    print('Situação: APROVADO COM DISTINÇÃO')
elif med >= 7 and med < 10:
    print(f'Média \t{med} pontos')
    print('Situação: APROVADO')
elif med < 7 and med >= 0:
    print(f'Média \t{med} pontos')
    print('Situação: REPROVADO')
else:
    print('Erro na digitação. Verifique as notas digitadas')