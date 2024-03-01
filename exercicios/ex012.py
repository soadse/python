prod = float(input('Qual é o preço do produto? R$ '))
desc = prod * 5 / 100
print('O valor do produto é {:.2f}R$, com um desconto de 5% ele sairá pelo valor de {:.2f}!'
      .format(prod, (prod - desc)))

