print('\n')
print('=--=' * 21)
print('A cada 1km acima da velocidade permitida será aplicada a multa de 7R$ ao contudor!')
print('=--=' * 21)
print('\n')
velocidade = float(input('Qual a velocidade do seu carro? '))
multa = velocidade - 80
if velocidade <= 80:
    print('Tudo ok!\nTenha um bom dia\nDirija com segurança sempre!')
else:
    print('Você foi mutado no valor de {:.2f}R$ por dirigir a cima da velocidade permitida de 80km por HR!'.format(multa * 7))
