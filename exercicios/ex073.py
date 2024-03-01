cont = cont2 = 0
cont3 = 16
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goiás', 'Coritiba', 'América-MG')
print('\033[1;33m=\033[m'*90)
print('{:^90}'.format('\033[1;32mTABELA DE CLASSIFICAÇAÕ DO BRASILEIRÃO\033[m'))
print('\033[1;33m=\033[m'*90)
for i in times:
    cont += 1
    if 0 < cont <= 10:
        print('\033[1;32m', end='')
    elif 10 < cont <= 16:
        print('\033[1;33m', end='')
    elif 16 < cont <= 20:
        print('\033[1;31m', end='')
    print(cont, '°', i)
    print('\033[m')
print('\n')

print('{:-^100}'.format('\033[1;32mOs 5 primeiros colocados na tabela do brasileirão\033[m'))
for primeiros in times[:5]:
    cont2 += 1
    print(cont2, '°', primeiros)
print('\n')

print('{:-^100}'.format('\033[1;31m4 Ultimos colocados na tabela:\033[m '))
for ultimos in times[-4:]:
    cont3 += 1
    print(cont3, '°', ultimos)
print('\n')

print(f'Times em ondem alfabética \033[1;35m{sorted(times)}\033[m\n')

escolha = int(input('Qual posição você gostaria de ver? '))
if 0 < escolha <= 10:
    print('\033[1;32m')
elif 10 < escolha <= 16:
    print('\033[1;33m')
elif 16 < escolha <= 20:
    print('\033[1;31m')

print('-=-'*10)
print(escolha, end='° ')
for i in times[escolha - 1]:
    print(i, end='')
print(' ')
print('-=-'*10)
