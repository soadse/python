real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 4.90
euro = real / 5.26
print('Com {:.2f} reais você pode comprar:\n{:.2f} dólares ou {:.2f} euros'.format(real, dolar, euro))

while True:
    s = 's'
    n = 'n'
    res = input('Deseja continuar a conversão? (s/n)')
    if res == s:
        real = float(input('Quanto dinheiro você tem na carteira? '))
        dolar = real / 4.90
        euro = real / 5.26
        print('Com {:.2f} reais você pode comprar:\n{:.2f} dólares ou {:.2f} euros'.format(real, dolar, euro))
    else:
        break