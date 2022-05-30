#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais
#gordo e o mais magro, para isso você deve fazer um programa que pergunte a cada um dos clientes da
#academia seu código, sua e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0
#(zero) no campo código. Ao encerrar o programa também dever ser informados os códigos e valores do cliente
#mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

cont_atleta = 0
soma_peso = 0
soma_altura = 0
while True:
    codigo = int(input('Código: '))
    if codigo == 0:
        break
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    cont_atleta += 1
    soma_altura += altura
    soma_peso += peso
    if cont_atleta == 1:
        maior_altura = altura
        cod_maior_altura = codigo
        menor_altura = altura
        cod_menor_altura = altura
        maior_peso = peso
        cod_maior_peso = peso
        menor_peso = peso
        cod_menor_peso = peso
    else:
        if altura > maior_altura:
            maior_altura = altura
            cod_maior_altura = codigo
        if altura < menor_altura:
            menor_altura = altura
            cod_menor_altura = codigo
        if peso > maior_peso:
            maior_peso = peso
            cod_maior_peso = codigo
        if peso < menor_peso:
            menor_peso = peso
            cod_menor_peso = codigo
print(f'O Atleta de Código {cod_maior_altura} é o Mais Alto - Medindo {maior_altura}m')
print(f'O Atleta de Código {cod_menor_altura} é o Mais Baixo - Medindo {menor_altura}m')
print(f'O Atleta de Código {cod_maior_peso} é o Mais Pesado - Pesando {maior_peso} Kg')
print(f'O Atleta de Código {cod_menor_peso} é o Mais Leve - Pesando {menor_peso} Kg')
print(f'A média de altura na Academia é de {(soma_altura / cont_atleta):.2f}m')
print(f'A média de peso na Academia é de {(soma_peso / cont_atleta):.2f} Kg')

