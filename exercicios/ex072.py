num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Digite um número de \033[1;33m0\033[m a \033[1;33m20\033[m: '))
    if 0 <= escolha <= 20:
        break
    print('\033[1;31mTente novamente\033[m. ', end='')
print(f'Você escolheu o número \033[34m{num[escolha]}\033[m!')
