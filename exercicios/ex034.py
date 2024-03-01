salario = float(input('Qual o salario do funcionário? '))
aumento15 = (salario * 15 / 100) + salario
aumento10 = (salario * 10 / 100) + salario
if salario <= 1250:
    print('A partir de agora seu novo salario tera um aumento de 15%!\n'
          'Agora seu novo salário é de R${:.2f}'.format(aumento15))
else:
    print('A partir do dia 10/03 seu salário de R${:.2f} passará a ser R${:.2f}.'
          ' Sendo assim recebendo um aumento de 10% em seu salario! PARABÉNS.'.format(salario, aumento10))
