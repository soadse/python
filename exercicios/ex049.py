num = int(input('Digite um número para ver sua tabuada: '))
for i in range(0, 11):
    print(num, 'x', i, '=', num*i)
print('=-' * 10)
while True:
    s = 's'
    n = 'n'
    r = input('Deseja continuar? (s/n) ')
    if r == s:
        num = int(input('Digite um número para ver sua tabuada: '))
        for i in range(0, 11):
            print(num, 'x', i, '=', num * i)
        print('=-' * 10)
    elif r == n:
        break
    else:
        print('\033[31mOpção Inválida\033[m')
