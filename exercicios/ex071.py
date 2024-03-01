print('='*30)
print('{:^40}'.format('\033[1;34mCAIXA ELETRONICO\033[m'))
print('='*30)
valor = float(input('Digite o valor do saque: R$'))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de \033[1;32m{total_cedula}\033[m cédulas de R$\033[1;32m{cedula}\033[m')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('='*30)
print('{:^40}'.format('\033[34mVOLTE SEMPRE!\033[m'))
