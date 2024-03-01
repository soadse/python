num = int(input('Digite um número: '))
print('O número é {}, seu antecessor é {} e seu sucessor é {}!'.format(num, (num - 1), (num + 1)))

while True:
     s = 's'
     n = 'n'
     res = input('Deseja continuar? (s/n)')
     if res == s:
        num = int(input('Digite um número: '))
        print('O número é {}, seu antecessor é {} e seu sucessor é {}!'.format(num, (num - 1), (num + 1)))
     else:
         break