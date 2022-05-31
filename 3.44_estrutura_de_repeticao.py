#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio dos códigos.
#Os códigos utilizados são 1, 2, 3 e 4 | 5 - Nulo | 6 - Branco
#Faça um programa que calcule e mostre:
# a) O total de votos para cada candidato
# b) O total de votos nulos
# c) O total de votos em branco
# d) A porcentagem de votos nulos sobre o total de votos
# e) A porcentagem de votos em branco sobre o total de votos
#Para finalizar o conjunto de votos tem-se o valor zero

c1 = c2 = c3 = c4 = b = n = v = 0
while True:
    print('#' * 26)
    print('CÉDULA DE VOTAÇÃO'.center(26))
    print('#' * 26)
    print('[1] - Quico')
    print('[2] - Chaves')
    print('[3] - Chiquinha')
    print('[4] - Sr. Madruga')
    print('[5] - Nulo')
    print('[6] - Branco')
    print('[0] - Sair')
    print('#' * 26)
    voto = int(input('Voto: '))
    if voto == 0:
        break
    while voto < 0 or voto > 6:
        voto = int(input('Digite um voto válido: '))
    v += 1
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        n += 1
    else:
        b += 1
print('#' * 26)
print('RESUMO DA VOTAÇÃO'.center(26))
print(f'Quico        {c1} votos')
print(f'Chaves       {c2} votos')
print(f'Chiquinha    {c3} votos')
print(f'Sr. Madruga  {c4} votos')
print(f'Votos Nulo   {n}')
print(f'Votos Branco {b}')
print('#' * 26)
print(f'Total de Votos: {v}')
print(f'Houve {(n/v)*100:.1f}% de Votos Nulos')
print(f'Houve {(b/v)*100:.1f}% de Votos Brancos')
