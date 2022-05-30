#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
#conveniências. Faça um programa que implemente uma caixa Registradora rudimentar. O programa deverá receber
#um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado
#pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o
#valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação,
#o programa deverá voltar ao ponto inicial, para regitrar a próxima compra. A saída deve ser conforme o exemplo.


soma_compra = 0
while True:
    codigo_produto = int(input('Código do Produto: [0 - para sair]: '))
    if codigo_produto == 0:
        break
    preco_produto = float(input('R$ '))
    soma_compra += preco_produto
dinheiro = float(input('Valor Pago: '))
print(f'Total da Compra: R${soma_compra:6.2f}')
print(f'Troco: R${dinheiro - soma_compra:6.2f}')

