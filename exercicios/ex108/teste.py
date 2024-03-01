import moeda

n = float(input('Digite o preço: R$'))
taxa = int(input('Qual o valor de desconto/taxa? '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando {moeda.taxa(taxa)} de {moeda.moeda(n)} temos {moeda.moeda(moeda.aumento(n, taxa))}')
print(f'Diminuindo {moeda.taxa(taxa)} de {moeda.moeda(n)} temos {moeda.moeda(moeda.diminuir(n, taxa))}')
