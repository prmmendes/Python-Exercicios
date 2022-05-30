#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
#cada eleitor votar e ao final mostrar o número de votos de cada candidato.

qte_eleitor = int(input('Qual o número de eleitores? '))
cassio = ronaldo = dida = invalido = 0
for v in range(1, qte_eleitor + 1):
    print('#' * 50)
    print('URNA ELETRÔNICA'.center(50))
    print('#' * 50)
    print('Escolha seu candidato: ')
    print('-' * 50)
    print('12 - CÁSSIO RAMOS')
    print('13 - RONALDO GIOVANELLI ')
    print('14 - DIDA')
    print('-' * 50)
    voto = int(input('Digite seu voto: '))
    if voto == 12:
        cassio += 1
    elif voto == 13:
        ronaldo += 1
    elif voto == 14:
        dida += 1
    else:
        invalido += 1
print('#' * 50)
print('APURAÇÃO DOS VOTOS: '.center(50))
print(f'12 - CÁSSIO: \t\t{cassio} votos válidos')
print(f'13 - RONALDO: \t\t{ronaldo} votos válidos')
print(f'14 - DIDA: \t\t\t{dida} votos válidos')
print(f'Votos inválidos: \t{invalido} votos')
print('#' * 50)


