vogais = ('A', 'E', 'I', 'O', 'U')
palavra = str(input('Digite uma palavra para ver suas vogais: ')).strip().upper()
print(f'A palavra digitada foi \033[1;33m{palavra}\033[m')
print('E ela tem: ', end='')
for p in palavra:
    if p in vogais:
        print('\033[1;33m', p, '\033[m', end=' ')
print(' como vogais')

palavras = ('aprender', 'programar', 'linguagem', 'python')
for pa in palavras:
    print(f'\nNa palavra \033[1;33m{pa.upper()}\033[m temos ', end='')
    for letra in pa:
        if letra.lower() in 'áãâaéèêeiôóouú':
            print(letra, end=' ')
            