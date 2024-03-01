a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite outro valor: '))
print('Os valores digitados foram: {} {} e {}!'.format(a, b, c))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado é {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é {}'.format(maior))
