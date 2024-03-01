def votação(idade):
    from datetime import date
    ano = date.today().year
    idade = ano - idade
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#Programa Principal
print('='*50)
nasc = int(input('{:^50}'.format('Em que ano você nasceu?\n')))
print('{:^50}'.format(votação(nasc)))
print('='*50)
