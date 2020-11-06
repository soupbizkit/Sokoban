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

    temporal  = output[0].split(',') # ['1','2']
    for i in temporal:
        jugadorPos.append(int(i))

    for i in range(1, len(output)):
        temporalCajas = output[i].split(',')
        cajasPos.append(convertirInt(temporalCajas))

    return jugadorPos, cajasPos, mapa, metas      
    #print(jugadorPos, cajasPos, mapa)
 

def convertirInt(listaStrings):
    listaResult = []
    for i in listaStrings:
        listaResult.append(int(i))
    return listaResult