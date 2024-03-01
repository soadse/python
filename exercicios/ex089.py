from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print('='*25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('='*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
print('='*25)
while True:
    print('='*45)
    per = int(input('Mostrar notas de qual aluno? (\033[31m999 interrompe\033[m)'))
    if per == 999:
        print('FINALIZANDO', end='')
        for c in range(0, 3):
            sleep(1)
            print('.', end='')
        break
    if per <= len(ficha) -1:
        print(f'Notas de {ficha[per][0]} são {ficha[per][1]}')
print()
print(f'{"Volte sempre!":^45}')
