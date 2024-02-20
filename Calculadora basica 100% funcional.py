import PySimpleGUI as sg
conta=0
layout = [
    [sg.Text('Conta'), sg.Input(key='Conta')],
    [sg.Button('=')]
]
janela=sg.Window('calculadora', layout)
while True:
    eventos,e= janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == '=':
        sg.popup(eval(e['Conta']))

#made by https://github.com/ANT0NI0737BR/codigos.git        