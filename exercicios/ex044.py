print('{:=^40}'.format('FORMA DE PAGAMENTO'))
valor = float(input('Digite o valor das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] À vista
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Pagando o valor de R${:.2f} á vista você recebera um desconto de 10%\nCom isso seu pagamento saira por R${:.2f}.'.format(valor, valor - (valor * 10 / 100)))
elif opção == 2:
    print('Pagando o valor de R${:.2f} á vista no cartão você recebera um desconto de 5%\nCom isso seu pagamento saira por R${:.2f}.'.format(valor, valor - (valor * 5 / 100)))
elif opção == 3:
    total = valor
    numero_de_parcelas = total / 2
    print('Pagando o valor de R${:.2f} parcelado em 2x no cartão não há desconto, mas também não acarretará juros.\nSuas parcelas serão de 2x de R${:.2f} SEM JUROS'.format(valor, numero_de_parcelas))
elif opção == 4:
    parcela = int(input('Qual o número de parcelas? '))
    numero_de_parcela_2 = valor / parcela
    print('Pagando o valor de R${:.2f} parcelado em {:.0f}x no cartão avera juros de 20%\nCom isso o valor passará a ser de R${:.2f}.'.format(valor, parcela, valor + (valor * 20 / 100)))
    print('Suas parcelas serão de {}x de R${:.2f} COM JUROS'.format(parcela, numero_de_parcela_2))
else:
    print('\033[1;31mOpção inválida\033[m')
