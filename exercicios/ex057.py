sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
if sexo == 'F':
    print('Você é do sexo Feminino!')
elif sexo == 'M':
    print('Você é do sexo Masculino!')
else:
    while sexo not in 'MnFf':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
        if sexo == 'F':
            print('Você é do sexo Feminino!')
        elif sexo == 'M':
            print('Você é do sexo Masculino!')
print('Sexo registrado com sucesso')
