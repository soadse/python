n1 = cont = soma = 0
n1 = int(input('Digite \033[31m999\033[m para parar: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Digite \033[31m999\033[m para parar: '))
print('você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
