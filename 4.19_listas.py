#Um empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em Servidores?"
# "As possíveis respostas são:
# 1 - Windows Server
# 2 - Unix
# 3 - Linux
# 4 - Netware
# 5 - Mac OS
# 6 - Outros
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
#O programa deverá ler os valores ate´ser informado o valor 0, que encerra a entrada de Dados. Não deverão ser aceitos
#valores além dos válidos para o Programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num
#vetor. Após os dados terem sido completamente informados, o programa deverá calcular o percentual de cada um dos concor-
#rentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

votos = [0,0,0,0,0,0]
sos = ('Windows Server', 'Unix          ', 'Linux         ', 'Netware       ', 'Mac OS        ', 'Outro         ')
while True:
    print('Qual o melhor Sistema Operacional para uso em Servidores?')
    print('-' * 25)
    print('[1] - Windows Server')
    print('[2] - Unix          ')
    print('[3] - Linux         ')
    print('[4] - Netware       ')
    print('[5] - Mac OS        ')
    print('[6] - Outro         ')
    print('-' * 25)
    voto = int(input('Digite seu voto: '))
    while voto < 0 or voto > 6:
        print('RESPOSTA INVÁLIDA! Escolha uma opção entre as disponíveis abaixo:')
        print('-' * 25)
        print('[1] - Windows Server')
        print('[2] - Unix')
        print('[3] - Linux')
        print('[4] - Netware')
        print('[5] - Mac OS')
        print('[6] - Outro')
        print('-' * 25)
        voto = int(input('Digite seu voto: '))
    if voto == 0:
        break
    votos[voto-1] += 1
print('Sistema Operacional \t\t Votos \t\t %')
soma_votos = sum(votos)
for s in range(6):
    print(f'{sos[s]} \t\t\t\t {votos[s]} \t\t {(votos[s] / soma_votos)*100:>.1f}')
print('-' * 30)
melhor_sistema = votos.index(max(votos))
print(f'O {sos[melhor_sistema]} foi o mais votado com {max(votos)}, que corresponde a {(max(votos) / sum(votos))*100:.1f}%')

