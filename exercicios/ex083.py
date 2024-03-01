inicio = 0
final = 0
exp = str(input('Digite uma expressão para ver se ela é válida:\n'))
for e in exp:
    if e == '(':
        inicio += 1
    elif e == ')':
        final += 1
if inicio == final:
    print('Sua expressão é \033[32mválida\033[m!')
elif inicio != final:
    print(f'Sua expressão é \033[31mfalsa\033[m!\nFalta \033[31m{inicio - final}\033[m expressão!')
