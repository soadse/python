print('-=' * 10)
print('\033[1;34m10 TERMOS DE UMA PA\033[m')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('\033[31mPAUSA\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\033[31mFIM\033[m\nProgressão finalizada com {} termos mostrados'.format(total))
