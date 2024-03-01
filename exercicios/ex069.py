idade = 0
cont_idade = 0
cont_sexo_m = 0
cont_sexo_f = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        cont_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo (M/F): ')).upper().strip()[0]
        if sexo == 'M':
            cont_sexo_m += 1
        if sexo == 'F' and idade < 20:
            cont_sexo_f += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? (S/N): ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {cont_idade}')
print(f'Ao todo foram {cont_sexo_m} homem(s) cadastrado(s).')
print(f'E temos {cont_sexo_f} mulher(es) com menos de 20 anos.')
