from time import sleep
cont = 0
tent = 3
nome = str(input('qual é seu nome? ')).capitalize().strip()
email = str(input('Crie um EMAIL:\n'))
senha = int(input('Crie uma SENHA somante com números:\n'))
login_email = str(input('Digite seu EMAIL: '))
while login_email != email:
    print('\033[31mEMAIL INVÁLIDO\033[m!')
    login_email = str(input('Digite novamente o EMAIL: '))
login_senha = int(input('Digite sua SENHA: '))
while login_senha != senha:
    print('\033[31mSENHA INVÁLIDA\033[m!')
    print(f'Você tem \033[31m{tent}\033[m tentativas!')
    login_senha = int(input('Digite novamente a SENHA: '))
    cont += 1
    tent -= 1
    if cont == 3:
        print('\033[35mUsuario bloqueado!\033[m')
        break
if login_senha == senha:
    for i in range(3):
        sleep(1)
        print('.', end='')
    print('\033[32mAcesso permitido\033[m')
    print(f'Seja bem-vindo {nome}')
