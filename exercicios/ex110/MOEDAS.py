def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def aumento(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('\033[1m-\033[m'*33)
    print('RESUMO DE VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumento(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*33)

