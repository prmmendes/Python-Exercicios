#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome de
#usuário, mostrando uma mensagem de erro e voltando a pedir as informações

nome = str(input('Login: '))
senha = str(input('Senha: '))
while nome.upper() == senha.upper():
    print('Erro! Senha igual ao nome de Usuário. Tente novamente')
    nome = str(input('Login: '))
    senha = str(input('Senha: '))
print('Cadastro concluído com SUCESSO!')