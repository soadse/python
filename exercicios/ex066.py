cont = soma = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos \033[34m{cont}\033[m valores foi \033[34m{soma}\033[m!')
