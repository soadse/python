from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
res = 0
while res != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    res = int(input('>>>>> O que você gostaria de fazer? '))
    if res == 1:
        print('\033[32mA soma de {} + {} é igual a {}.\033[m'.format(n1, n2, (n1 + n2)))
    elif res == 2:
        print('\033[32mO resultado de {} x {} é igual a {}.\033[m'.format(n1, n2, (n1 * n2)))
    elif res == 3:
        if n1 > n2:
            print('\033[32mEntre {} e {} o maior é {}.\033[m'.format(n1, n2, n1))
        else:
            print('\033[32mEntre {} e {} o maior é {}.\033[m'.format(n1, n2, n2))
    elif res == 4:
            print('\033[31mInforme os números novamente:\033[m ')
            n1 = int(input('1° Novo valor: '))
            n2 = int(input('2° Novo valor: '))
    elif res == 5:
        print('\033[31mFinalizando\033[m')
        for i in range(5):
            print('.', end='')
            sleep(0.5)
    else:
        print('\033[1;31mOpção invalida\033[m. Tente novamente.')
    print('-=-' * 10)
    sleep(2)
print('Fim do programa.\nVolte sempre!')
