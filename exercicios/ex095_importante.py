from time import sleep
time = list()
ficha = dict()
gols = list()
final = 'Finalizando...'
print('='*50)
print(f'{'\033[33mPROGRAMA DE PARTIDAS DE FUTEBOL\033[m':^57}')
print('='*50)
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome do jogador: ')).capitalize()
    qnts = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
    gols.clear()
    for c in range(0, qnts):
        gols.append(int(input(f'Quantos gols na {c+1} partida?')))
    ficha['gols'] = gols[:]
    ficha['total'] = sum(gols)
    time.append(ficha.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('='*50)
print('cod ', end='')
for i in ficha.keys():
    print(f'{i:<15}', end='')
print()
print('='*50)
for k, v in enumerate(time):
    print(f' {k} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\033[31mERRO! Não existe jogador com o codigo {busca}\033[m')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  - Na {i+1}° partida fez {g} gols')
    print('-'*50)
for f in final:
    sleep(0.3)
    print('\033[31m', f, '\033[m', end='')
print()
print(f'{'\033[34mVolte sempre\033[m':^55}')
