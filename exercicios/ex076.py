print('-'*60)
print('{:^60}'.format('MATERIAL ESCOLAR'))
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-'*60)
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.90,
            'Compaso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<50}', end='')
    else:
        print(f'R$ \033[1m{produtos[posicao]:>7.2f}\033[m')
