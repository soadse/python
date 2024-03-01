numero = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(numero, 'x', i, '=', numero * i)

    while True:
        s = 's'
        n = 'n'
        res = input('Deseja continuar? (s/n)')
        if res == s:
            numero = int(input('Digite um número para ver sua tabuada: '))
            for i in range(1, 11):
                print(numero, 'x', i, '=', numero * i)
            print(12 * '-')
        else:
            break