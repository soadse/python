from random import randint
from time import sleep
tentativas = 0
parabens = '''\n\n
________´$$$$`_____________________________,,,_
_______´$$$$$$$`___________________________´$$$`
________`$$$$$$$`______,,________,,_______´$$$$´
_________`$$$$$$$`____´$$`_____´$$`____´$$$$$´
__________`$$$$$$$`_´$$$$$`_´$$$$$`__´$$$$$$$´
___________`$$$$$$$_$$$$$$$_$$$$$$$_´$$$$$$$´_
____________`$$$$$$_$$$$$$$_$$$$$$$`´$$$$$$´_
___,,,,,,___`$$$$$$_$$$$$$$_$$$$$$$_$$$$$$´_
_´$$$$$`____`$$$$$$_$$$$$$$_$$$$$$$_$$$$$$´_
´$$$$$$$$$`´$$$$$$$_$$$$$$$_$$$$$$$_$$$$$´_
´$$$$$$$$$$$$$$$$$$_$$$$$$$_$$$$$$$_$$$$$´_
___`$$$$$$$$$$$$$$$_$$$$$$$_$$$$$$_$$$$$$´_
______`$$$$$$$$$$$$$_$$$$$__$$_$$$$$$_$$´_
_______`$$$$$$$$$$$$,___,$$$$,_____,$$$$$´_
_________`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$´_
__________`$$$$$$$$$$$$$$$$$$$$$$$$$$$´_
____________`$$$$$$$$$$$$$$$$$$$$$$$$´_
--------------`$$$$$$$$$$$$$$$$$$$$$´-
_______________`$$$$$$$$$$$$$$$$$$$$´_ '''
maquina = (randint(0, 9),
           randint(0, 9),
           randint(0,9))
'''for m in maquina:
    print(m, end='  ')'''
print('\033[1;35m=--\033[m'*30,)
print('{:^150}'.format('''
                          ╔═════════════ ஜ۩۞۩ஜ ════════════╗'
                 '.·★·.♥ ·.         \033[1;35mDESCUBRA A SENHA\033[m       .·★·.♥ ·.'
                         '╚═════════════ ஜ۩۞۩ஜ ════════════╝\n'''))
print('\033[1;35m=--\033[m'*30)
print('\nSerá que você consegue descobrir a senha que eu criei?')
print('Vamos lá...')
for ponto in range(5):
    print('.', end=' ')
    sleep(0.3)
while True:
    tentativa = ((int(input('\nDigite \033[1m3\033[m números: \n'))),
                 int(input('')),
                 int(input('')))
    if tentativa == maquina:
        break

    if tentativa[0] < maquina[0]:
        print(f'\033[32mO primeiro número é maior do que o que você digitou\033[m!')
    elif tentativa[0] > maquina[0]:
        print(f'\033[31mO primeiro número é menor do que o que você digitou!\033[m')
    else:
        print(f'\033[34mO Primeiro número está certo!\033[m')

    if tentativa[1] < maquina[1]:
        print(f'\033[32mO segundo número é maior do que o que você digitou\033[m!')
    elif tentativa[1] > maquina[1]:
        print(f'\033[31mO segundo número é menor do que o que você digitou\033[m!')
    else:
        print('\033[34mO segundo número está certo!\033[m')

    if tentativa[2] < maquina[2]:
        print(f'\033[32mO terceiro número é maior do que o que você digitou!\033[m')
    elif tentativa[2] > maquina[2]:
        print(f'\033[31mO terceiro número é menor do que o que você digitou!\033[m')
    else:
        print('\033[34mO terceiro número está certo!\033[m')

    tentativas += 1


print('{:^100}'.format(parabens))
print('\n\033[1;34mVOCÊ ACERTOU\033[m!\n')
print('Você digitou')
for t in tentativa:
    print('\033[1;32m',t,'\033[m', end=' ')
print('\ne minha senha é')
for m in maquina:
    print('\033[1;32m',m,'\033[m', end=' ')

print(f'Você acertou com {tentativas -1} tentativas!')
