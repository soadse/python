lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado, não irei adicionar!\033[m')
    continuar = str(input('Deseja continuar? [\033[32mS\033[m/\033[31mN\033[m] ')).upper()
    if continuar == 'N':
        break
print('='*50)
lista.sort()
print(f'Você adicionou os números: {lista}')
print('='*50)
