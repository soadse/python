from time import sleep
def valores(* num):
    cont = maior = 0
    print('\033[35m-=\033[m'*20)
    print('Analisando os valores passados....')
    sleep(1)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
valores(2, 5, 7, 9, 3)
valores(1, 2, 4)
