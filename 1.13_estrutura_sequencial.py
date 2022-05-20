#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite sua altura: '))
ph = (72.7 * altura) - 58
pm = (62.1 * altura) - 44.7
print(f'Considerando a altura {altura}m o peso ideal é {ph:.1f}Kg para homens e {pm:.1f}Kg e para mulheres')
