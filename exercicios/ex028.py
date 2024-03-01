from random import randint
from time import sleep
computador = randint(1, 5)
print('-==-' * 11)
print('Vou pensar em um número. Tente adivinhar...')
print('-==-' * 11)
sleep(2)
print('Pensando....')
sleep(3)
jogador = int(input('Pensei em um número de 1 a 5! Qual foi o número? '))
print('Analisando...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer! Eu pensei no número {}!'.format(computador))
else:
    print('Você errou! Eu pensei no número {} e não no {}'.format(computador, jogador))
print('-==-' * 12)
print('\n')
while True:
    s = 's'
    n = 'n'
    res = str(input('Deseja continuar? (s/n)\n'))
    print('\n')
    if res == s:
        computador = randint(1, 5)
        print('-==-' * 11)
        print('Vou pensar em um número. Tente adivinhar...')
        print('-==-' * 11)
        sleep(2)
        print('Pensando....')
        sleep(3)
        jogador = int(input('Pensei em um número de 1 a 5! Qual foi o número? '))
        print('Analisando...')
        sleep(2)
        if jogador == computador:
            print('Parabéns! Você conseguiu me vencer! Eu pensei no número {}!'.format(computador))
        else:
            print('Você errou! Eu pensei no número {} e não no {}'.format(computador, jogador))
        print('-==-' * 12)
        print('\n')
