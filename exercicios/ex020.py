from random import shuffle
n1 = input('Digite um nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação vai ser: {}'.format(lista))
