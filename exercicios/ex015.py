dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você rodou com o carro? '))
pago1 = dias * 60
pago2 = km * 0.15
print('O total a pagar ppor dias alugados é de {:.2f}!'.format(pago1))
print('O total a pagar por km rodado é de {:.2f}!'.format(pago2))
print('O total a pagar é de {}!'.format(pago1 + pago2))
