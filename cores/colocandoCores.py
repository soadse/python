'''
        style    background
          ↓       ↓
     \033[0; 33; 44m
              ↑
            text

style              text                 back
0 = None           30 = Branco          40 = Branco
1 = Bold           31 = Vermelho        41 = Vermelho
4 = Underline      32 = Verde           42 = Verde
7 = Negative       33 = Amarelo         43 = Amarelo
                   34 = Azul            44 = Azul
                   35 = Roxo            45 = Roxo
                   36 = Ciano           46 = Ciano
                   37 = Cinza           47 = Cinza
                                                        '''
print('\033[0;30;41m Teste')
print('\033[4;33;44m Teste')
print('\033[1;35;43m Teste')
print('\033[30;42m Teste')
print('\033[m Teste')
print('\033[7;30m Teste')