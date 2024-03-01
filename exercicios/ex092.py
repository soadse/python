from datetime import datetime
from time import sleep
fim = 'FIM DO PROGRAMA'
ficha = dict()
while True:
    ficha['nome'] = str(input('Nome: ')).capitalize()
    ficha['idade'] = int(input('Ano de nascimento: '))
    ficha['idade'] = datetime.now().year - ficha["idade"]
    ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if ficha['ctps'] == 0:
        break
    print('\033[31mMinimo de 35 anos trabalhados!\033[m')
    ficha['contratação'] = int(input('Ano da contratação: '))
    ficha['salário'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contratação'] + 35) - datetime.now().year)
    print(f'{'--------- DADOS DO TRABALHADOR ----------':^50}')
    for k, v in ficha.items():
        print(f' - {k}: {v}')
    print(f'O trabalhador ira se aposentar no ano de: {ficha['contratação'] + 35}')
    print(f'O trabalhador ira se aposentar com {ficha['aposentadoria']} anos de idade.')
    break
for f in fim:
    sleep(0.5)
    print('\033[31m', f, '\033[m', end='')
