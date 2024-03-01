numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar: [S/N] ')).upper()
    if r == 'N':
        break
print('='*40)
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')

if 5 not in numeros:
    print('O valor 5 não foi encontrado dentro da lista')
elif 5 in numeros:
    print('O valor 5 está entre os números')
