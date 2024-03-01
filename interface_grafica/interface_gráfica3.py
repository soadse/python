import requests
from tkinter import *
def bom_dia():
    txt = 'Tudo Bem?'

    texto2['text'] = txt


def carregar():
    ola = 'ola'

    texto3['text'] = ola

janela = Tk()
janela.title('Rodrigo')
janela.geometry('400x300')

texto1 = Label(janela, text='Seja Bem-Vindo')
texto1.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Bom dia', command=bom_dia)
botao.grid(column=0, row=1, padx=10, pady=10)

botao2 = Button(janela, text='Clique Aqui', command=carregar)
botao2.grid(column=0, row=3, padx=10, pady=10)

texto2 = Label(janela, text='')
texto2.grid(column=0, row=2, padx=10, pady=10)

texto3 = Label(janela, text='')
texto3.grid(column=0, row=4, padx=10, pady=10)







janela.mainloop()
