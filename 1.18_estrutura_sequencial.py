#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
#Internet em (Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

tam_arq = int(input('Tamanho do arquivo em MB: '))
vel_dow = int(input('Velocidade do Link em Mbps: '))
conversao = tam_arq * 8
tempo = conversao / vel_dow
minutos = tempo / 60
print(f'Serão gastos {minutos:.2f} minutos')
