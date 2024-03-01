from datetime import date
atual = date.today().year
total_maior = 0
toatal_menor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = atual - nasc
    if idade >= 21:
        total_maior += 1
    else:
        toatal_menor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(total_maior))
print('E também tivemos {} pessoas menores de idade'.format(toatal_menor))
