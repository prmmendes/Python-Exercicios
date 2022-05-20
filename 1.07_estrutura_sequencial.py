#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadr = float(input('Digite em centimetros o lado de um quadrado: '))
area = quadr * quadr
print(f'A área do quadrado, cujos lados possuem {quadr}cm é de {area}cm')
print(f'O dobro desta área é {area*2}cm')