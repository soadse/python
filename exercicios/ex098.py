from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(0.4)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.4)
        print('FIM')


def linha():
    print('-'*30)


# Programa Principal
contador(1, 10, 1)
linha()
contador(10, 0, 2)
sleep(1)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
