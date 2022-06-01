#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes form lidas. Imprima as consoantes

cont = 0
letras = list()
for l in range(0, 10):
    letras.append(str(input('Digite uma letra: ')))
print('Consoantes digitadas -->', end=' ')
for c in letras:
    if c not in 'AaEeIiOu12345+67890+-*/\|,.;<>:}][{ºª/?°¹²³£¢¬!@#$%¨&*()_-§=+':
        print(c,end=' ')
        cont += 1
print(f'\nForam digitados {cont} consoantes')
