print('-=-' * 10)
print('18.5: Abaixo do peso;\n18.5 até 25: Peso ideal;\n25 até 30: Sobrepeso;'
      '\n30 até 40: Obesidade;\nAcima de 40: Obesidade Mórbida.')
print('-=-' * 10)

peso = float(input('Digite seu peso: kg '))
altura = float(input('Digite sua altura: M '))
imc = peso / (altura ** 2)
print('O \033[1;32mIMC\033[m dessa pessoa é de {:.1f} '.format(imc), end='')
if imc < 18.5:
    print('\033[31mAbaixo do peso\033[m!')
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal\033[m!')
elif 25 <= imc < 30:
    print('\033[31mSobrepeso\033[m!')
elif 30 <= imc < 34.9:
    print('\033[31mObesidade grau I\033[m!')
elif 35 <= imc < 39.9:
    print('\033[31mObesidade grau II\033[m!')
else:
    print('\033[31mObesidade Mórbida\033[m!')
    print('Obesidade grau III!')
