def expandirNodo(nodo):
    return 1

def direccionAgente(mapa, jugadorPos, cajasPos):
    return 1

def percepcion(jugadorPos,mapa, cajasPos):
                    #UP,     DONW,   LEFT,    RIGHT
    movimientos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    movesResult = []

    for i in movimientos:
      nuevaPos =[jugadorPos[0] + i[0], jugadorPos[1] + i[1]] #encuentra la nueva posicion del jugador
      print(nuevaPos)

      if cajaCercana(i, nuevaPos, cajasPos): #Verifica si hay 2 cajas en fila hacia esa dirección
        continue

      if mapa[nuevaPos[0]][nuevaPos[1]] == 'W':
        continue
      elif i == [-1, 0]:
        movesResult.append('U')
      elif i == [1, 0]:
        movesResult.append('D')
      elif i == [0, -1]:
        movesResult.append('L')
      elif i == [0, 1]:
        movesResult.append('R')
    #print(movesResult)
    return movesResult
    
def cajaCercana(movimiento, nuevaPos, cajasPos):
    otraCaja = False
    for i in cajasPos: 
      if nuevaPos == i:
        posibleCaja = [nuevaPos[0] + movimiento[0], nuevaPos[1] + movimiento[1]] 
        for j in cajasPos:
          if j == posibleCaja:
            otraCaja = True
          else:
            otraCaja
    return otraCaja

def camino():
    return 1

#retorna true o false si las cajas están en la posición de las metas          
def victoria(metas, cajasPos):
  gano = False
  sortedCajas= sorted(cajasPos)
  sortedMetas = sorted(metas)
  if sortedCajas == sortedMetas:
    gano = True
  else:
    gano = False
  return gano

