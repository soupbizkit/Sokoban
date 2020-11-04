import sys 

def leerMapa():
    mapa = []
    output = []
    jugadorPos = []
    cajasPos = []
    for line in sys.stdin:
        line = line.rstrip()
        if line.startswith('W') or line.startswith('0'):  
            mapa.append(line)
        else:
            output.append(line)
        
    jugadorPos = output[0]
    for i in range(1, len(output)):
        cajasPos.append(output[i])

    return jugadorPos, cajasPos, mapa      
    #print(jugadorPos, cajasPos, mapa)
 
