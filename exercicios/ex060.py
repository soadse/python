n = int(input('Digite um número para ver seu \033[32mFATORIAL\033[m: '))
c = n
f = 1
print('Calculando {}!\n'.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
