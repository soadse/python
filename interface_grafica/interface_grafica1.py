import PySimpleGUI as sg
sg.theme('DarkPurple')
layout = [[sg.Text('Usuario')],
          [sg.InputText()],
          [sg.Text('Senha:')],
          [sg.InputText()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Iniciar sessão', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
window.close()
