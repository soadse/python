from random import randint
from time import sleep
from operator import itemgetter
jg = {'jogador 1': randint(1, 6),
      'jogador 2': randint(1, 6),
      'jogador 3': randint(1, 6),
      'jogador 4': randint(1, 6)}
ranking = list()
print('='*50)
print(f'{'VALORES SORTEADOS':^50}')
print('='*50)
print('🎲 '*16)
for k, v in jg.items():
    sleep(1)
    print(f'{k}: tirou... {v:>22} no dado.')
sleep(1)
print('🎲 '*16)
sleep(1)
ranking = sorted(jg.items(), key=itemgetter(1), reverse=True)
print(f'{'\033[33m== RANKING DO GANHADORES ==\033[m':^60}')
print()
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}° lugar: {v[0]} {v[1]:>24} pontos')
sleep(1)
print()
print(f'{'\033[31m🏆 Parabéns 🏆\033[m':^58}')
sleep(1)
for i, v in enumerate(ranking):
    print(f'{f'{v[0]}, ganhou com {v[1]} pontos':^52}')
    break
