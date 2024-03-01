print('-'*45)
print('{:^50}'.format('\033[1;36mLOJA SUPER BARATÃO\033[m'))
print('-'*45)
total = 0
total_mil = 0
produto_menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        total_mil += 1
    if cont == 1:
        produto_menor = preco
        barato = produto
    else:
        if preco < produto_menor:
            produto_menor = preco
            barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:-^40}'.format('\033[1;31mFIM DO PROGRAMA\033[m'))
print(f'O total da compra foi de R$\033[1;32m{total:.2f}\033[m')
print(f'Temos {total_mil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${produto_menor:.2f}')
