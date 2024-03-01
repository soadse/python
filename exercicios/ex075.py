numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores \033[1;34m{numeros}\033[m')
print(f'O número 9 apareceu {numeros.count(9)} vez(es)!')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}ª')
else:
    print('O número 3 não foi digitado em nenhuma posição!')
print('Os números \033[1;33mpares\033[m digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print('\033[3;33;2m', n, end=' ' '\033[m')
