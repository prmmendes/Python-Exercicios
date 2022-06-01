#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve
#perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim
#calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar
#o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos
#terem respondido informar:
# a) Maior e Menor Acerto;
# b) Total de Alunos que utilizaram o sistema
# c) A Média das Notas da Turma
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova
#antes dos alunos usuarem o programa

print('Inserir Gabarito')
q1 = str(input('1 - Letra: ')).upper()
while q1 != 'A' and q1 != 'B' and q1 != 'C' and q1 !='D' and q1 != 'E':
    q1 = str(input('Digite uma Letra válida: ')).upper()
q2 = str(input('2 - Letra: ')).upper()
while q2 != 'A' and q2 != 'B' and q2 != 'C' and q2 !='D' and q2 != 'E':
    q2 = str(input('Digite uma Letra válida: ')).upper()
q3 = str(input('3 - Letra: ')).upper()
while q3 != 'A' and q3 != 'B' and q3 != 'C' and q3 !='D' and q3 != 'E':
    q3 = str(input('Digite uma Letra válida: ')).upper()
q4 = str(input('4 - Letra: ')).upper()
while q4 != 'A' and q4 != 'B' and q4 != 'C' and q4 !='D' and q4 != 'E':
    q4 = str(input('Digite uma Letra válida: ')).upper()
q5 = str(input('5 - Letra: ')).upper()
while q5 != 'A' and q5 != 'B' and q5 != 'C' and q5 !='D' and q5 != 'E':
    q5 = str(input('Digite uma Letra válida: ')).upper()
q6 = str(input('6 - Letra: ')).upper()
while q6 != 'A' and q6 != 'B' and q6 != 'C' and q6 !='D' and q6 != 'E':
    q6 = str(input('Digite uma Letra válida: ')).upper()
q7 = str(input('7 - Letra: ')).upper()
while q7 != 'A' and q7 != 'B' and q7 != 'C' and q7 !='D' and q7 != 'E':
    q7 = str(input('Digite uma Letra válida: ')).upper()
q8 = str(input('8 - Letra: ')).upper()
while q8 != 'A' and q8 != 'B' and q8 != 'C' and q8 !='D' and q8 != 'E':
    q8 = str(input('Digite uma Letra válida: ')).upper()
q9 = str(input('9 - Letra: ')).upper()
while q9 != 'A' and q9 != 'B' and q9 != 'C' and q9 !='D' and q9 != 'E':
    q9 = str(input('Digite uma Letra válida: ')).upper()
q10 = str(input('10 - Letra: ')).upper()
while q10 != 'A' and q10 != 'B' and q10 != 'C' and q10 !='D' and q10 != 'E':
    q10 = str(input('Digite uma Letra válida: ')).upper()
preencher = 'S'
cont = 0
soma_pontos = 0
while True:
    cont += 1
    pontos = 0
    nome = str(input('Nome: '))
    print('Digite suas respostas')
    r1 = str(input('Questão 1: ')).upper()
    if r1 == q1:
        pontos += 1
    r2 = str(input('Questão 2: ')).upper()
    if r2 == q2:
        pontos += 1
    r3 = str(input('Questão 3: ')).upper()
    if r3 == q3:
        pontos += 1
    r4 = str(input('Questão 4: ')).upper()
    if r4 == q4:
        pontos += 1
    r5 = str(input('Questão 5: ')).upper()
    if r5 == q5:
        pontos += 1
    r6 = str(input('Questão 6: ')).upper()
    if r6 == q6:
        pontos += 1
    r7 = str(input('Questão 7: ')).upper()
    if r7 == q7:
        pontos += 1
    r8 = str(input('Questão 8: ')).upper()
    if r8 == q8:
        pontos += 1
    r9 = str(input('Questão 9: ')).upper()
    if r9 == q9:
        pontos += 1
    r10 = str(input('Questão 10: ')).upper()
    if r10 == q10:
        pontos += 1
    soma_pontos += pontos
    print(f'Aluno: {nome} | {pontos} pontos')
    print('#' * 30)
    perg = int(input('Digite 0 para sair: '))
    if cont == 1:
        maior_nota = pontos
        melhor_aluno = nome
        menor_nota = pontos
        pior_aluno = nome
    if pontos > maior_nota:
        maior_nota = pontos
        melhor_aluno = nome
    if pontos < menor_nota:
        menor_nota = pontos
        pior_aluno = nome
    if perg == 0:
        break
print(f'{cont} alunos fizeram a Avaliação')
print(f'{soma_pontos / cont:.1f} pontos foi a Média da Turma')
print(f'O melhor desempenho foi do aluno {melhor_aluno} com nota {maior_nota} pontos')
print(f'O pior desempenho foi do aluno {pior_aluno} com nota {menor_nota} pontos')

