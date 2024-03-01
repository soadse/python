from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        if n % 2 == 0:
            n = f'\033[34m{n}\033[m'
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            print(f'\033[34m{v}\033[m', end=' ')
            soma += v
    print(f'A soma dos valores pares da lista é \033[34m{soma}\033[m')


numeros = list()
sorteia(numeros)
somaPar(numeros)
