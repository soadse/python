import customtkinter
janela = customtkinter.CTk()
janela.geometry('500x300')

def clique():
    bv = 'Seja Bem-Vindo'

    msg['text'] = bv




texto = customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack()

email = customtkinter.CTkEntry(janela, placeholder_text='E-mail')
email.pack()

senha = customtkinter.CTkEntry(janela, placeholder_text='Senha', show='*')
senha.pack()

botao = customtkinter.CTkButton(janela, text='Login', command=clique)
botao.pack()

msg = customtkinter.CTkLabel(janela, text='')
msg.pack()

janela.mainloop()
