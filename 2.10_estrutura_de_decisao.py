#Faça um programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V - Vespertino
# ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme
# o caso.

print('=-'*16)
print(f'TURNO DE ESTUDO.'.center(32))
print('=-'*16)
print('[M] - Matutino')
print('[V] - Vespertino')
print('[N] - Noturno')
print('=-'*16)
turno = str(input('Digite o turno que você estuda: ')).upper()
if turno == 'M':
    print('BOM DIA! SEJA BEM VINDO!')
elif turno == 'V':
    print('BOA TARDE! SEJA BEM VINDO!')
elif turno == 'N':
    print('BOA NOITE! SEJA BEM VINDO!')
else:
    print('VALOR INVÁLIDO!')