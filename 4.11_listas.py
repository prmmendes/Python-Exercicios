#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetorA = []
vetorB = []
vetorC = []
vetorD = []
print('Vetor A')
for a in range(10):
    vetorA.append(int(input(f'Vetor A | {a+1}º número: ')))
print('*' * 28)
print('Vetor B')
for b in range(10):
    vetorB.append(int(input(f'Vetor B | {b+1}º número: ')))
print('*' * 28)
print('Vetor C')
for c in range(10):
    vetorC.append(int(input(f'Vetor C | {c+1}º número: ')))
for d in range(10):
    vetorD.append(vetorA[d])
    vetorD.append(vetorB[d])
    vetorD.append(vetorC[d])
print('Vetor A -->', end=' ')
for i, a in enumerate(vetorA):
    if i < len(vetorA) - 1:
        print(f'{a} |', end=' ')
    else:
        print(a)
print('Vetor B -->', end=' ')
for i, b in enumerate(vetorB):
    if i < len(vetorB) - 1:
        print(f'{b} |', end=' ')
    else:
        print(b)
print('Vetor C -->', end=' ')
for i, c in enumerate(vetorC):
    if i < len(vetorC) - 1:
        print(f'{c} |', end=' ')
    else:
        print(c)
print('Vetor D -->', end=' ')
for i, d in enumerate(vetorD):
    if i < len(vetorD) - 1:
        print(f'{d} |', end=' ')
    else:
        print(d)

