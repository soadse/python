galera = list()
ficha = dict()
soma = media = 0
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: ')).capitalize()
    ficha['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while ficha['sexo'] not in 'MF':
        print('\033[31mERRO!\033[m Por favor, digite apenas M ou F.')
        ficha['sexo'] = str(input('Sexo: [M/F] ')).upper()
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    galera.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO!\033[m Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
for g in galera:
    print(g)
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print()
print(f'B) A média de idade é de {media:5.2f}')
print()
print('C) As mulheres cadastradas foram:')
for f in galera:
    if f['sexo'] in 'F':
        print(f'- {f["nome"]} ')
print()
print(f'D) Lista de pessoas que estão acima da média:')
for f in galera:
    if f['idade'] >= media:
        for k, v in f.items():
            print(f'- {k} = {v};')
        print('-'*30)
print(f'{'\033[31mFim do programa\033[m':^40}')
