print('Viajando a cima de 200km você ganhará um desconto')
distancia = int(input('Qual a distância da sua viagem? '))
d1 = 0.50
d2 = 0.45
if distancia <= 200:
    print('Sua viagem saira pelo valor de R${:.2f}'.format(distancia * d1))
else:
    print('Você recebeu um desconto promocional por viajar a cima de 200km!\nCom isso, você pagará o valor de R${:.2f}!'.format(distancia * d2))
