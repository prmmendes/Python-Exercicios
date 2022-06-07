#Sua Organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com intenção de fazer
#um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testas todos os cerca de 200 mouses
#que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
#número indeterminado de entradas, cada uma contendo: um número de identificação do mouse e o tipo de defeito:
# a) necessita da esfera
# b) necessita de limpeza
# c) necessita do cabo ou conector
# d) quebrado ou inutilizado.
#Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

defeito = ('Necessita da Esfera          ', 'Necessita de Limpeza         ',
           'Necessita do Cabo ou Conector', 'Quebrado ou Inutilizado      ')
tipo_defeitos = [0, 0, 0, 0]
cont = 0
while True:
    print('=-_' * 15)
    print('REGISTRO DO TIPO DE DEFEITO'.center(45))
    print('=-_' * 15)
    print('[1] - Necessita da Esfera')
    print('[2] - Necessita de Limpeza')
    print('[3] - Necessita troca do Cabo ou Conector')
    print('[4] - Quebrado ou Inutilizado')
    tipo = int(input('Tipo do Defeito: '))
    while tipo < 0 or tipo > 4:
        print('=-_' * 15)
        print('REGISTRO DO TIPO DE DEFEITO'.center(45))
        print('Escolha Inválida! Tente Novamente!'.center(45))
        print('=-_' * 15)
        print('[1] - Necessita da Esfera')
        print('[2] - Necessita de Limpeza')
        print('[3] - Necessita troca do Cabo ou Conector')
        print('[4] - Quebrado ou Inutilizado')
        tipo = int(input('Faça um escolha válida: '))
    if tipo == 0:
        break
    tipo_defeitos[tipo - 1] += 1
    cont += 1
print('=-_' * 15)
print('RELATÓRIO DE DEFEITOS'.center(45))
print(f'Quantidade de Mouses: {cont}')
print('=-_' * 15)
print('Situação                                Quantidade           Percentual')
for d in range(4):
    print(f'[{d+1}] - {defeito[d]}\t\t {tipo_defeitos[d]}\t\t\t\t\t\t {tipo_defeitos[d] / sum(tipo_defeitos)*100:>.1f}%')