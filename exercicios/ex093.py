ficha = dict()
gols = list()
print('='*50)
print(f'{'\033[33mPROGRAMA DE PARTIDAS DE FUTEBOL\033[m':^57}')
print('='*50)
ficha['nome'] = str(input('Nome do jogador: ')).capitalize()
qnts = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
for c in range(1, qnts + 1):
    gols.append(int(input(f'Quantos gols na {c} partida?')))
ficha['gols'] = gols[:]
ficha['total'] = sum(gols)
print('-'*50)
print(ficha)
print('-'*50)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*50)
print(f'O jogador {ficha['nome']} jogou {qnts} partidas.')
for i, v in enumerate(gols):
    print(f' => Na partida {i+1}, fez {v} gols')
