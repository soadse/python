print('-※-' * 20)
print('\033[31mProgama de financiamento de imóvel\033[m')
print('-※-' * 20)
casa = float(input('Digite o valor do imóvel que você gostaria de comprar: R$'))
salario = float(input('Digite o valor do seu salario: R$'))
anos = int(input('Em quantos anos você deseja pagar?: '))
prestacao = casa / (anos * 12)
porcento = salario * 30 / 100
if prestacao <= porcento:
    print('Emprestimo \033[32mAPROVADO!\033[m\nCom o salário de R${:.2f}, financiando um imovel de R${:.2f} por {} anos, você pode!!!!'.format(salario, casa, anos))
    print('Seu números de parcelas sairá por R${:.2f}'.format(prestacao))
else:
    print('Emprestio \033[31mNEGADO!\033[m\nCom o salário de R${:.2f}, financiando um imovel de R${:.2f} por {} ano, você não pode!!!!'.format(salario, casa, anos))
    print('Seu número de parcelas excede o valor de 30% de seu salário')
