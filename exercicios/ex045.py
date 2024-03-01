from random import randint
from time import sleep
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[maquina]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 11)
if maquina == 0: # computador jogou pedra
    if jogador == 0:
        print('\033[31mEMPATE\033[m!')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[34mMÁQUINA VENCE\033[m')
    else:
        print('Jogada Invalida!')

elif maquina == 1: # computador jogou papel
    if jogador == 0:
        print('\033[34mMÁQUINA VENCE\033[m')
    elif jogador == 1:
        print('\033[31mEMPATE\033[m!')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCE\033[m')
    else:
        print('Jogada Invalida!')

elif maquina == 2: # computador jogou tesoura
    if jogador == 0:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[34mMÁQUINA VENCE\033[m')
    elif jogador == 2:
        print('\033[31mEMPATE\033[m!')
    else:
        print('Jogada Invalida!')
