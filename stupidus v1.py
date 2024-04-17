import PySimpleGUI as sg
import random as rd
import time as tm


tempo = 2 #duração entre a repetição do codigo

tempoinicio = float(tm.time()) 

numerodevezes = 0

contador = 0

corvermelho = ('#FF0000', '#6A0000')
corverde = ('#00FF00', '#00AA00')
corazul = ('#0055FF', '#001744')
coramarelo = ('#FFFF00', '#5C5C00')

sequencia = ['corazul','corvermelho', 'corazul']

sequenciajog = []

completo = False

def sortearcor():
    
    cor = ''

    random = rd.randint(1,4)
    
    if random == 1:
        cor = 'corazul'

    elif random == 2:
        cor = 'corverde'

    elif random == 3:
        cor = 'coramarelo'

    elif random == 4:
        cor = 'corvermelho'

    sequencia.append(cor)

def mudarcor(contador):

    Janela[f'{(sequencia[contador])}'].update(button_color=('black', f'{eval((sequencia[contador])+"[1]")}' ))







jogo = [
    [sg.Button('azul', key='corazul', size=(10,10), button_color=('black', corazul[0]), font=('arial', 15)), sg.Button('vermelho', key='corvermelho', size=(10,10), button_color=('black', corvermelho[0]), font=('arial', 15))],
    [sg.Button('amarelo', key='coramarelo', size=(10,10), button_color=('black', coramarelo[0]), font=('arial', 15)), sg.Button('verde', key='corverde', size=(10,10), button_color=('black', corverde[0]), font=('arial', 15))],
    [sg.Text('', key='tempo')]
]

Janela = sg.Window("stupidus",jogo,finalize=True)
#Janela.maximize()
while True:

    tempodesdoinicio = ((tm.time()) - tempoinicio - ((tempo * numerodevezes))) #a quanto tempo o programa está rodando

    e,v = Janela.read(timeout=100)

#input_jogador

    if e == 'corazul':
    
        sequenciajog.append('corazul')

    elif e == 'coramarelo':
    
        sequenciajog.append('coramarelo')

    elif e == 'corverde':
    
        sequenciajog.append('corverde')

    elif e == 'corvermelho':
    
        sequenciajog.append('corvermelho')

    print()
    print(f'contador: {contador}')
    print(f'len(jog): {len(sequenciajog)}')
    print(f'{sequenciajog}')
    print(f'len(seq): {len(sequencia)}')
    print(f'{sequencia}\n------------------')


#fim_input_jogador

    if contador == len(sequencia) and completo == False: #verifica se todas as cores já foram mostradas

        completo = True

    if e == sg.WINDOW_CLOSED:
        break

    if contador != len(sequencia) and completo == False:

        mudarcor(contador)

    if tempodesdoinicio > tempo and completo == False: #loop, executa o codigo dentro dele a cada 2 segundos

        numerodevezes = numerodevezes + 1

        Janela[f'{(sequencia[contador])}'].update(button_color=('black', f'{eval((sequencia[contador])+"[0]")}' ))
    
        contador = contador + 1


    if len(sequenciajog) == len(sequencia) or len(sequenciajog) > len(sequencia): #verificar acerto

        if sequenciajog == sequencia:

            sg.popup('acertou')

            sequenciajog = []

            sortearcor()

            completo = False

            contador = - 1



        else:
            
            sg.popup('errou')

            sequenciajog = []

            completo = False

            contador = - 1

#made by https://github.com/ANT0NI0737BR