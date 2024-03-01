from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ')
for n in numeros:
    print('\033[1;34m', n, end='   \033[m')
print(f'\nO maior valor sorteado foi o número \033[1;32m{max(numeros)}\033[m')
print(f'O menor valor sorteado foi o número \033[1;31m{min(numeros)}\033[m')
