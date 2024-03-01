from random import randint
from time import sleep
sorte = 'FIM DO PROGRAMA'
lista = list()
jogos = list()
print('{:^138}'.format('='*40))
print('{:^150}'.format('\033[3;35mJOGO DA MEGA SENA\033[m'))
print('{:^138}'.format('='*40))
quant = int(input(f'{'Quantos jogos você quer fazer? ':^140}'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append((num))
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('{:^150}'.format(f'\033[1;34mSORTEANDO {quant} JOGOS...\033[m'))
print()
for i, l in enumerate(jogos):
    sleep(1)
    print('{:^140}'.format(f'Jogo {i+1}: {l}'))
print()
sleep(1)
print('{:^140}'.format(f'----------< BOA SORTE >----------'))
print()
for s in sorte:
    sleep(0.2)
    print(f'\033[31m{s:^10}\033[m', end='')
