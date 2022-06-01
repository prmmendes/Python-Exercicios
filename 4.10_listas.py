#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
#valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetorA = []
vetorB = []
vetorC = []
print('Vetor A')
for a in range(10):
    vetorA.append(int(input(f'{a+1}º Valor: ')))
print('*' * 20)
for b in range(10):
    vetorB.append(int(input(f'{b+1}º Valor: ')))
for c in range(10):
    vetorC.append(vetorA[c])
    vetorC.append(vetorB[c])
print('Vetor A -->', end=' ')
for i, a in enumerate(vetorA):
    if i < len(vetorA) - 1:
        print(f'{a} |', end=' ')
    else:
        print(a)
print('Vetor B -->', end=' ')
for i, b in enumerate(vetorB):
    if i < len(vetorA) - 1:
        print(f'{b} |', end=' ')
    else:
        print(b)
print('Vetor C -->', end=' ')
for i, c in enumerate(vetorC):
    if i < len(vetorC) - 1:
        print(f'{c} |', end=' ')
    else:
        print(c)
