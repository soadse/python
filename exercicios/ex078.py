num = []
menor = maior = 0
for c in range(0, 5):
    num. append(int(input(f'Dígite um valor para a posição {c + 1}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('='*50)
print('{:^50}'.format(f'Você digitou os valores {num}'))
print(f'O maior número digitado foi \033[32m{maior}\033[m na posição', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'\033[34m{i + 1}\033[m...', end=' ')
print()
print(f'O menor valor digitado foi \033[31m{menor}\033[m na posição', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'\033[34m{i + 1}\033[m...', end=' ')
print()
print('='*50)
