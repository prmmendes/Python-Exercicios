#Faça um programa que leia e valide as seguintes informações:
# a) Nome: maior que 3 caracteres
# b) Idade: entre 0 e 150
# c) Salário: maior que 0
# d) Sexo: 'F' ou 'M'
# e) Estado Civil: 'S', 'C', 'V', 'D'

nome = str(input('Nome: '))
idade = int(input('Idade: '))
salario = float(input('Salário: R$ '))
sexo = str(input('[M]asculino | [F]eminino: ')).upper()
est_civil = str(input('[S]olteiro | [C]asado | [V]iúvo | [D]ivorciado ')).upper()
while len(nome) <= 3:
    print('Nome deve ter mais que 3 caracteres. Tente novamente.')
    nome = str(input('Nome: '))
while idade < 0 or idade > 150:
    print('Idade inválida! Tente novamente.')
    idade = int(input('Idade: '))
while salario <= 0:
    print('Salário inválido! Salário precisa ser maior que R$ 0,00')
    salario = float(input('Salário: R$ '))
while sexo not in 'FM':
    print('Digite um sexo válido. Escolha em [M] ou [F].')
    sexo = str(input('Sexo: ')).upper()
while est_civil not in 'SCVD':
    print('Erro! Escolha um Estado Civil válido: [S]olteiro | [C]asado | [V]iúvo | [D]ivorciado ')
    est_civil = str(input('Estado Civil: ')).upper()
if sexo == 'M':
    tsexo = 'Masculino'
else:
    tsexo = 'Feminino'
if est_civil == 'S':
    test_civil = 'Solteiro'
elif est_civil == 'C':
    test_civil = 'Casado'
elif est_civil == 'V':
    test_civil = 'Viúvo'
else:
    test_civil = 'Divorciado'
print('#'*50)
print('CADASTRO CONCLUÍDO COM SUCESSO!'.center(50))
print(f'{nome}'.center(50))
print(f'{idade} anos'.center(50))
print(f'Salario - R$ {salario:.2f}'.center(50).replace('.',','))
print(f'Sexo - {tsexo}'.center(50))
print(f'Estado Civil - {test_civil}'.center(50))
print('#'*50)
