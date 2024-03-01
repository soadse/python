'''def leiaInt(numero):
    while True:
        print('-'*33)
        numero = str(input('Digite um número: ')).upper()
        if numero.isnumeric():
            numero = int(numero)
            print(f'Você digitou o número {numero}')
            break
        else:
            print(f'\033[31mERRO\033[m. {numero} não é um número!')
            print(f'Digite um número válido.')
        print('-'*30)


leiaInt('Digite um valor: ')'''
#--------------------------------------------------------------------------------------------------------------------#
def leiAint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor


n = leiAint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
