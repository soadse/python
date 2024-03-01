from random import choice
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
while True:
    s = 's'
    n = 'n'
    p1 = input('Deseja continuar o sorteio? (s/n) ')
    if p1 == s:
        n1 = input('Digite o nome do aluno: ')
        n2 = input('Digite o nome do segundo aluno: ')
        n3 = input('Digite o nome do terceiro aluno: ')
        n4 = input('Digite o nome do quarto aluno: ')
        lista = [n1, n2, n3, n4]
        escolhido = choice(lista)
        print('O aluno escolhido foi {}'.format(escolhido))
    else:
        break
        