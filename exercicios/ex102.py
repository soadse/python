def fatorial(n, show=False):
    """
    \033[35m-> Função para calcular o fatorial de um númmero.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número N.\033[m
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

help(fatorial)

num = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(num, True))
