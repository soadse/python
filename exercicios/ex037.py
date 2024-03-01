num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('A conversão do número {} para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('A conversão do número {} para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('A conversão do número {} para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida!\033[m')
