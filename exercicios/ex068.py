from random import randint
print('=-'*20)
print('\033[34mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('=-'*20)
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    maquina = randint(1, 10)
    total = jogador + maquina
    par_impar = str(input('Par ou Ímpar? [P/I] ')).upper()
    if par_impar == 'P':
        if total % 2 == 0:
            print('Você \033[34mGANHOU\033[m!')
            print(f'Você escolheu \033[32m{jogador}\033[m e o computador escolheu \033[32m{maquina}\033[m e a soma de ambas escolhas foi de \033[32m{total}\033[m')
            vitoria += 1
        else:
            print('Você \033[31mPERDEU\033[m!')
            print(f'Você escolheu \033[32m{jogador}\033[m e o computador escolheu \033[32m{maquina}\033[m e a soma de ambas escolhas foi de \033[32m{total}\033[m')
            print('\033[1mDeu Impar\033[m' if total % 2 == 1 else '\033[1mDeu Par\033[m')
            print('Você escolheu \033[31mPAR\033[m')
            break

    elif par_impar == 'I':
        if total % 2 == 1:
            print('Você \033[34mGANHOU\033[m!')
            print(f'Você escolheu \033[32m{jogador}\033[m e o computador escolheu \033[32m{maquina}\033[m e a soma de ambas escolhas foi de \033[32m{total}\033[m')
            vitoria += 1
        else:
            print('Você \033[31mPERDEU\033[m!')
            print(f'Você escolheu \033[32m{jogador}\033[m e o computador escolheu \033[32m{maquina}\033[m e a soma de ambas escolhas foi de \033[32m{total}\033[m')
            print('\033[1mDeu Par\033[m' if total % 2 == 0 else '\033[1mDeu Impar\033[m')
            print('Você escolheu \033[31mIMPAR\033[m')
            break
print(f'Você ganhou \033[34m{vitoria}\033[m vezes!')
