def notas(*n, sit=False):
    """\033[35m
    Função para saber as notas.
    :param n: Valores das notas
    :param sit: (Opcional) para ver ou não a situação das notas
    :return: (DICIONÁRIO) Retorna o TOTAL, MAIOR, MENOR e a MÉDIA das notas
    \033[m"""
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

help(notas)
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
