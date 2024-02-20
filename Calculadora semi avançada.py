t=""
import PySimpleGUI as sg
sg.theme("reds")
layout=[command:workbench.trust.manage
[sg.Button("CC"),sg.Text(key="t"),],
[sg.Button("1"),sg.Button("2"),sg.Button("3"),sg.Button("-")],
[sg.Button("4"),sg.Button("5"),sg.Button("6"),sg.Button("+")],
[sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button("/")],
[sg.Button("="),sg.Button("0"),sg.Button("x²"),sg.Button("x")]
]
j=sg.Window("calculadora",layout)

while True:
        e1,e2= j.read()

        if e1 == sg.WINDOW_CLOSED:
            break
        if e1 =='1':
            y="1"
            t=t+y
            j['t'].update(t)
        if e1 =='2':
            y="2"
            t=t+y
            j['t'].update(t)
        if e1 =='3':
            y="3"
            t=t+y
            j['t'].update(t)
        if e1 =='4':
            y="4"
            t=t+y
            j['t'].update(t)
        if e1 =='5':
            y="5"
            t=t+y
            j['t'].update(t)
        if e1 =='6':
            y="6"
            t=t+y
            j['t'].update(t)
        if e1 =='7':
            y="7"
            t=t+y
            j['t'].update(t)
        if e1 =='8':
            y="8"
            t=t+y
            j['t'].update(t)
        if e1 =='9':
            y="9"
            t=t+y
            j['t'].update(t)
        if e1 =='0':
            y="0"
            t=t+y
            j['t'].update(t)
        if e1 =='-':
            y="-"
            t=t+y
            j['t'].update(t)
        if e1 =='+':
            y="+"
            t=t+y
            j['t'].update(t)
        if e1 =='/':
            y="/"
            t=t+y
            j['t'].update(t)
        if e1 =='x':
            y="*"
            t=t+y
            j['t'].update(t)
        if e1 =='x²':
            y="**2"
            t=t+y
            j['t'].update(t)

        if e1 =='=':
            int=t
            a=eval(t)
            j['t'].update(a)
        
        if e1 =="CC":
            t=""
            j['t'].update(t)
            
#made by https://github.com/ANT0NI0737BR/codigos.git       