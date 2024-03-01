nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, amédia do aluno é: {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('Sua nota foi {}, com isso você foi aprovado! \033[1;32mPARABÉNS\033[M'.format(media))
elif media >= 5 and media < 7: # ou 7 > media >= 5
    print('Sua note foi {}, por isso você estará de recuperação!'.format(media))
else:
    print('Sua nota foi {}, por isso você foi \033[1;31mREPROVADO\033[m'.format(media))
