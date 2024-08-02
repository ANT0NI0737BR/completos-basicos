import random as rd

def gerarcadeia():

    #dna1  dna2    rna1   rna2
    # a ---> t ---> a ---> u
    # t ---> a ---> u ---> a
    # g ---> c ---> g ---> c
    # c ---> g ---> c ---> g

    DNAbases = (
    ('a', 'g'),
    ('t', 'c')
    )

    DNAnomes = (
    ('adenina', 'guanina'),             #puricas
    ('timina','citosina')  #pirimídicas
    )

    RNAbases = (
    ('a', 'g'),
    ('u', 'c')
    )

    RNAnomes = (
    ('adenina', 'guanina'),
    ('uracila', 'citosina')
    )

    contador = 0
    tamanho = (3*rd.randint(3,4))

    cadeiadna1 = []                     #1° fita de dna
    cadeiadna2 = []                     #2° fita de dna
    cadeiarna1 = []                     #copia da 1° fita de dna
    cadeiarna2 = []                     #copia da 2° fita de dna

    while contador != tamanho:

        tipo = rd.randint(0,1)          # 0- puricas | 1- pirimídicas

        if tipo == 0:
            qual = rd.randint(0,1)

        else:
            qual = rd.randint(0,1)

        base = DNAbases[tipo][qual]

        cadeiadna1.append(base)

        contador += 1

    contador2 = 0

    while contador2 != len(cadeiadna1):

        if cadeiadna1[contador2:contador2+1][0] == 'a':  
            cadeiadna2.append('t')
            cadeiarna1.append('a')
            cadeiarna2.append('u')
        
        elif cadeiadna1[contador2:contador2+1][0] == 't':
            cadeiadna2.append('a')
            cadeiarna1.append('u')
            cadeiarna2.append('a')

        elif cadeiadna1[contador2:contador2+1][0] == 'c':
            cadeiadna2.append('g')
            cadeiarna1.append('c')
            cadeiarna2.append('g')
        
        elif cadeiadna1[contador2:contador2+1][0] == 'g':
            cadeiadna2.append('c')
            cadeiarna1.append('g')
            cadeiarna2.append('c')

        contador2 += 1

    return(cadeiadna1,cadeiadna2,cadeiarna1,cadeiarna2)


contador = 0

acertos = 0
erros = 0

bases = gerarcadeia() # 0 = dna1 | 1 = dna2 | 2 = rna1 | 3 = rna 2


todasrespostas = ['',]
acertadas = [0,0,0]

while True:


    if contador == 3:

        print(f'=====\n|FIM|\n=====\nerros: {erros} | acertos: {acertos}')
        print(f'\ngabarito:')

        c = 0
        while c != 4:

            print(f'{'RNA' if c > 1 else 'DNA'}: {legivel[c]} {'-inicial-' if c == 0 else '-dada-'} {todasrespostas[c]} {'erro' if acertadas[c-1] == 0 else ''}')
            c += 1

        break


    resdada = []

    legivel = [''.join(str(e) for e in bases[0]),''.join(str(e) for e in bases[1]),''.join(str(e) for e in bases[2]),''.join(str(e) for e in bases[3])]




    print(f'traduza essa fita para outra fita de {''.join('RNA' if contador > 0 else 'DNA')}.\n\n:{''.join(str(e) for e in bases[contador])}')


    r = str(input(':'))

    todasrespostas.append(r)


    for x in r:

        resdada.append(x)
    

    if resdada == bases[contador+1]:

        print('acerto\n---------------------\n')

        contador += 1

        acertos += 1 

        acertadas[contador-1] = 1


    else:

        print('erro\n---------------------\n')

        contador += 1

        erros += 1

        acertadas[contador-1] = 0

#made by https://github.com/ANT0NI0737BR