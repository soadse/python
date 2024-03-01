num = soma = cont = maior = menor = 0
resp = 's'.lower().strip()[0]
while resp == 's':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? (\033[32ms\033[m/\033[31mn\033[m) ')).lower().strip()[0]
print('Você digitou \033[34m{}\033[m números e sua soma é \033[34m{}\033[m.'.format(cont, soma))
print('Sua média foi de \033[34m{:.1f}\033[m'.format(soma / cont))
print('O maior número digitado foi \033[34m{}\033[m e o menor foi \033[34m{}\033[m'.format(maior, menor))
