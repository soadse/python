import moeda

n = float(input('Digite o preço: R$'))
taxa = int(input('Qual o valor de desconto/taxa? '))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é {moeda.dobro(n)}')
print(f'Aumentando {taxa}% de R${n}, temos {moeda.aumento(n, taxa)}')
print(f'Diminuindo {taxa}% de R${n}, temos {moeda.diminuir(n, taxa)}')
