salario = float(input('Qual é o salário do funcionário? '))
novo_salario = salario + (salario * 15 / 100)
print('O salario do funcionario é de {:.3f}R$!\n'
      'Com o aumento de 15%, ele passará a ser de {:.3f}R$!'.format(salario, novo_salario))
