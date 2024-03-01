print('\033[1;41mTeste de cores!\033[m')
v1 = input('Escolha uma cor:\nAzul\nAmarelo\nVermelho\n')
azul = 'Azul'
amarelo = '\033[1;33mAmarelo\033[m'
vermelho = '\033[1;31mVermelho\033[m'
if v1 == 'azul':
    print('Você escolhoeu a cor {}{}{}!'.format('\033[1;34m', azul, '\033[m'))
elif v1 == 'amarelo':
    print('Você escolheu a cor {}!'.format(amarelo))
elif v1 == 'vermelho':
    print('Você escolheu a cor {}!'.format(vermelho))
else:
    print('Cor inválida!')

#ou

v2 = input('Digite seu nome: ')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m'}
print('Olá {}{}{}'.format(cores['amarelo'], v2, cores['limpa']))
'''                                      ↑
                                precisa só mudar aqui           '''
