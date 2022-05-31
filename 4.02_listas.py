#Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

lista = list()
for c in range(1, 11):
    numero = float(input(f'Digite o {c} valor: '))
    lista.append(numero)
newlista = lista.__reversed__()
print('Lista -->', end=' ')
for l in lista:
    print(f'{l}', end=' | ')
print()
print('Lista Invertida -->', end=' ')
for r in newlista:
    print(f'{r}', end=' | ')
print()