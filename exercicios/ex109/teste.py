import moeda

n = float(input('Digite o preço: R$'))
taxa = int(input('Qual o valor de desconto/taxa? '))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'Aumentando {moeda.taxa(taxa)} de {moeda.moeda(n)} temos {moeda.aumento(n, taxa, True)}')
print(f'Diminuindo {moeda.taxa(taxa)} de {moeda.moeda(n)} temos {moeda.diminuir(n, taxa, True)}')
