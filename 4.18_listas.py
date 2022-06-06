#Uma grande emissora de televisão quer fazer um enquete entre os seus telespectadores para saber qual o melhor jogador
#após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
#para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem Python.
#Para computar cada voto, a telefonista digitará um número entre 1 e 23, correspondente ao número da camisa do jogador.
#Um número de jogador igual a zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa
#deve ignorá-lo, mostrando uma mensagem de aviso, e voltando a pedir outro número. Após a votação, o programa deverá
#exibir:
# a) O total de votos computados.
# b) Os números e respectivos votos de todos os jogadores que receberam votos.
# c) O percentual de votos de cada um destes jogadores.
# d) O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual
#de votos dados a ele.
#Observe que os votos inválidos  e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
#número do jogador. O programa deve fazer o uso de arrays. O programa deverá executar o calculo do percentual de cada
#jogador através de uma função. Está função receberá os parâmetros: o número de votos de um jogador e o total de votos.
#A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. A disposição das
#informações deve ser o mais proxio possivel ao exemplo. Os dados fictícios podem mudar a cada execução do programa.
#Ao final, o programa deve ainda gravar os dados referentes ao resultado final da votação em um arquivo texto no disco,
#obedecendo a mesma disposição apresentada na tela.

votos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print('^~v' * 20)
print('ENQUETE: Quem foi o melhor jogador da Partida?'.center(60))
print('^~v' * 20)
while True:
    voto = int(input('Nº do Jogador (0 = Fim): '))
    while voto < 0 or voto > 23:
        voto = int(input('VOTO INVÁLIDO! Escolha um número de 0 a 23 (0 para Sair): '))
    if voto == 0:
        break
    votos[voto-1] += 1
soma_votos = sum(votos)
print('Nº do Jogador\t\tQte de Votos\t\tPorcentagem')
for i, v in enumerate(votos):
    print(f'Jogador nº {i+1:>2} \t\t{v}\t\t\t\t\t{(v/soma_votos)*100:>.1f}%')
print(f'O melhor jogador foi o Nº {votos.index(max(votos))+1}, com {max(votos)} votos, correspondente a {(max(votos)/soma_votos)*100:>.1f}% dos votos')
