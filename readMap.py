import sys 

def leerMapa():
    mapa = []
    output = []
    jugadorPos = []
    metas = []
    cajasPos = []
    for line in sys.stdin:
        line = line.rstrip()
        if line.startswith('W') or line.startswith('0'):  
            mapa.append(line)
        else:
            output.append(line)
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'X':
                metas.append([i,j])

    jugadorPos = output[0]
    for i in range(1, len(output)):
        cajasPos.append(output[i])

    return jugadorPos, cajasPos, mapa, metas      
    #print(jugadorPos, cajasPos, mapa)
 
