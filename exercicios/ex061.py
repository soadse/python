print('-=' * 10)
print('\033[1;34m10 TERMOS DE UMA PA\033[m')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('\033[31mFIM\033[m')