n = []
pares = []
impares = []
while True:
    n.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r == 'N':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa de números digitados é: {n}')
print(f'Os números pares foram {pares}')
print(f'Os números ímpares foram {impares}')
