def jogador(nome, gols):
    if nome == '':
        return f'O jogador <DESCONHECIDO> fez {gols} gol(s) no campeonato.'
    if gols == '':
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    if nome == '' and gols == '':
        return f'O jogador <DESCONHECIDO> fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'



n = str(input('Nome do jogador: ')).capitalize()
g = str(input('Números de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
print(jogador(n, g))
