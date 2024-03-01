print('=' * 30)
print('\033[1;34m10 TERMOS DE UMA PA\033[m')
print('=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print(i, end=' ')
