def fatorial(n):

    lis = []

    for x in range(n):
        lis.append(x+1)

    cercas = len(lis)-1

    for x in range(cercas):

        g = lis[0] * lis[1]
        lis.pop(0)
        lis.pop(0)
        lis.append(g)
    return(lis[0])


#---------------------------------------------------
print(fatorial(4))
#made by https://github.com/ANT0NI0737BR/codigos.git    