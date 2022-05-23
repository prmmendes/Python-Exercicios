#Faça um programa que verifique se uma letra digitada é vogal ou consoante

letra = str(input('Digite uma letra qualquer: '))
if letra.upper() in 'AEIOU':
    print(f'Letra digitada [{letra}] - VOGAL')
else:
    print(f'Letra digitada [{letra}] - CONSOANTE')