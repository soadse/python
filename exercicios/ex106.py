print('\033[30;44m-='*75)
print(f'{'SISTEMA DE AJUDA PyHELP':^140}')
print('-='*75)
print('\033[m')
def ajuda(com):
    print('\033[30;41m')
    print('{:^140}'.format(f'Acessando o manual do comando {com}'))
    print()
    print('\033[m', end='')
    print('\033[7;40m')
    help(com)
    print('\033[m')


comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    print()
    if comando.upper() == 'FIM':
        print('\033[1;31m')
        print(f'{'Volte Sempre!':^140}')
        print('\033[m')
        break
    else:
        ajuda(comando)
