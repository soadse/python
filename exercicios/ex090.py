aluno = dict()
aluno['nome'] = str(input('Nome: ')).capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = '\033[32mAprovado\033[m'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = '\033[33mRecuperação\033[m'
else:
    aluno['situação'] = '\033[31mReprovado\033[m'
print('='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print('='*30)
print(f'Aluno {aluno["situação"]}')
