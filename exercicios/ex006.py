num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O número é {}, seu dobre é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(num, dobro, triplo, raiz))

while True:
    s = 's'
    n = 'n'
    res = input('Deseja continuar? (s/n)')
    if res == s:
        num1 = int(input('Digite um número: '))
        print('O número é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}!'.format(num1, (num1 * 2),
                                                                                                (num1 * 3),
                                                                                                (num1 ** (1 / 2))))
    else:
        break
