from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos de idade!'.format(idade))
if idade <= 9:
    print('Você é um nadador MIRIM.')
elif idade <=  14:
    print('Você é um nadador INFANTIL.')
elif idade <= 19:
    print('Você é um nadador JUNIOR.')
elif idade <= 25:
    print('Você é um nadador SÊNIOR.')
else:
    print('Você é um nadador MASTER.')
