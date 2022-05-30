#Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média
#da turma varia entre 0 e 25, 26 e 60 ou maior que 60. E então dizer se a turma é jovem, adulta ou idosa,
#conforme a média calculada.

n_pessoas = soma_idade = 0
while True:
    idade = int(input('Idade: '))
    n_pessoas += 1
    soma_idade += idade
    perg = str(input('Deseja cadastrar novo membro? [S]im ou [N]ão? ')).upper()
    while perg not in 'SN':
        perg = str(input('Responda corretamente! Deseja cadastrar mais pessoas? [S]im ou [N]ão')).upper()
    if perg == 'N':
        break
media = soma_idade / n_pessoas
print(f'Foram cadastradas {n_pessoas} pessoas')
print(f'A média de idade do grupo é de {media:.1f} anos')
if media <= 25:
    print('Este é um grupo JOVEM!')
elif media >25 and media <60:
    print('Este é um grupo ADULTO!')
else:
    print(f'Este é um trupo IDOSO')
