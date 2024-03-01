from datetime import date
atual = date.today().year
print('\033[31m-==-\033[m' * 10)
print('Progama de ALISTAMENTO MILITAR')
print('\033[31m-==-\033[m' * 10)
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))
if idade == 18:
    print('Você deve se alistar \033[31mIMEDIATAMENTE\033[m!')
elif idade > 18:
    print('Você já passou da data de alistamento! Seu ano de alistamento foi em {}'.format(atual - (idade - 18)))
else:
    saldo = 18 - idade
    print('Você ainda vai se alistar! Seu ano de alistamento vai ser em {}'.format(atual + saldo))
