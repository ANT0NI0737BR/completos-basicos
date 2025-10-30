def fatorial(n):

    if n != 0:
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
    else:
        return(1)

def permutação_caotica(n):

    lis = []
    Fn = fatorial(n)


    for x in range(n+1):
        lis.append((((-1)**x)/fatorial(x))*Fn)

    cercas = len(lis)-1


    for x in range(cercas):
        
        g = lis[0] + lis[1]
        lis.pop(0)
        lis.pop(0)
        lis.append(g)

    return(lis)



#---------------------------------------------------
#print(permutação_caotica(int(input(":"))))
#made by https://github.com/ANT0NI0737BR/codigos.git    