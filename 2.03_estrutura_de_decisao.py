#Faça um programa que verifique se uma letra digitada é 'F' ou 'M'. Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.

print('='*30)
print('ESCOLHA O SEXO'.center(30))
print('='*30)
print('[F] - Para Feminino')
print('[M] - Para Masculino')
print('='*30)
sexo = str(input('Escolha sua opção: ')).upper()
print('='*30)
if sexo == 'F':
    print('Sexo escolhido: FEMININO')
elif sexo == 'M':
    print('Sexo escolhido: MASCULINO')
else:
    print('Sexo escolhido: SEXO INVÁLIDO')