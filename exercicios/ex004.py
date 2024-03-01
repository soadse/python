a = input('Digite algo: ')
print('O tipo primimitivo desse valor é: ',type(a))
print('Só tem espaços? ', a.isspace())
print('È um número? ', a.isnumeric())
print('È alfabético? ', a.isalpha())
print('È alfaNumérico? ', a.isalnum())
print('Esta em maiúsculo? ', a.isupper())
print('Esta em minúsculo? ', a.islower())
print('Esta em capitalizada? ', a.istitle())

while True:
    s = 's'
    n = 'n'
    r = input('Deseja continuar? (s/n) ')
    if r == s:
        a = input('Digite algo: ')
        print('O tipo primimitivo desse valor é: ', type(a))
        print('Só tem espaços? ', a.isspace())
        print('È um número? ', a.isnumeric())
        print('È alfabético? ', a.isalpha())
        print('È alfaNumérico? ', a.isalnum())
        print('Esta em maiúsculo? ', a.isupper())
        print('Esta em minúsculo? ', a.islower())
        print('Esta em capitalizada? ', a.istitle())
    else:
        break