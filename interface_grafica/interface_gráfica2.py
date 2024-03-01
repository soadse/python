import tkinter
janela = tkinter.Tk()
janela.geometry('300x300')
janela.title('Ola')
meulabel = tkinter.Label(janela, text='Olá, Mundo')
meulabel.pack()
nome = tkinter.Label(janela, text='Qual seu nome? ')
nome.pack()
caixa = tkinter.Button(janela, text='Deseja continuar? ')
caixa.pack()

janela.mainloop()
