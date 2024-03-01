from random import randint
maquina = randint(1, 10)
print('Sou seu computador....Acabei de pensar em um número entre 1 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == maquina:
        acertou = True
    elif jogador < maquina:
        print('\033[32mMais\033[m')
    elif jogador > maquina:
        print('\033[31mMenos\033[m')
print('Acertou com \033[34m{}\033[m tentativas!'.format(palpites))
