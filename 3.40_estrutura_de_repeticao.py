#Foi feita uma estatistica em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
#Foram obtidos os seguintes dados:
# a) Código da Cidade
# b) Número de veículos de passeio:
# c) Número de acidentes de trânsito com vítimas..
# d) Qual o maior e o menor indice de acidentes de trânsito e a que cidade pertence.
# e) Qual a média de veículos nas cinco cidades juntas
# f) Qual a média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio.

soma_veiculos = 0
for a in range(1, 6):
    cod_cidade = int(input('CEP: '))
    veiculos = int(input('Quantidade de veículos de Passeio: '))
    acidentes = int(input('Números de acidentes de trânsito (ano): '))
    soma_veiculos = soma_veiculos + veiculos
    if a == 1:
        maior_indice = acidentes
        cod_maior = cod_cidade
        menor_indice = acidentes
        cod_menor = cod_cidade
    if acidentes > maior_indice:
        maior_indice = acidentes
        cod_maior = cod_cidade
    if acidentes < menor_indice:
        menor_indice = acidentes
        cod_menor = cod_menor
    soma_veiculos = soma_veiculos + veiculos
    if veiculos < 2000:
        print(f'A Cidade {cod_cidade}, que possui {veiculos} veículos, tem média de {acidentes / veiculos} acidentes')
print(f'A média de veículos nas 5 cidades é de: {soma_veiculos / 5:.1f}')
print(f'O maior indice de acidentes de Trânsito é na cidade {cod_maior}, com {maior_indice} acidentes')
print(f'O menor indice de acidentes de Trânsito é na cidade {cod_menor}, com {menor_indice} acidentes')



