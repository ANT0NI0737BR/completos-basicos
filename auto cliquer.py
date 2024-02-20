import time as tm
import keyboard as kb

tecla = str('w')                                                                 #tecla que vai ser pressionada

periodo = float(2)                                                               #tempo em segundos entre pressionamentos

tempoinicio = float(tm.time())                                                   #pega o tempo em que o programa foi iniciado

numerodevezes = 0

while True:

    tempodesdoinicio = ((tm.time()) - tempoinicio - (periodo * numerodevezes))   #a quanto tempo o programa está rodando

    if (kb.is_pressed('+')) == True:                                             #para o codigo ao apertar +

        break

    if tempodesdoinicio > periodo:
         
        kb.send(tecla)                                                           #pressiona a tecla

        numerodevezes = numerodevezes + 1                                        #conta quantas vezes o botão já foi pressionado

        print(tempodesdoinicio)                                                  #DEBUG-tempo des do inicio do programa

        print(f'w foi presionado {numerodevezes} vezes')

#made by https://github.com/ANT0NI0737BR/codigos.git       
    