def percepcion(jugadorPos, mapa, cajasPos, metas):
                    #UP,     DONW,   LEFT,    RIGHT
    movimientos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    movesResult = []

    for i in movimientos:
      nuevaPos =[jugadorPos[0] + i[0], jugadorPos[1] + i[1]] #encuentra la nueva posicion del jugador

      if cajaCercana(i, nuevaPos, cajasPos): #Verifica si hay 2 cajas en fila hacia esa dirección
        continue

      if cajaContraPared(i, nuevaPos, cajasPos, mapa):
        continue

      #if cajaEnMeta(nuevaPos, cajasPos, metas):#Verifica si la caja que se tiene delante se puede mover o no
        #continue

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

"""def cajaEnMeta(nuevaPos, cajasPos, metas):
  enMeta = False
  for caja in cajasPos: 
      if nuevaPos == caja:
        for meta in metas:
          if caja == meta:
            enMeta = True
          else:
            enMeta
  return enMeta"""
    
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

def camino(nodo):
  camino = []
  camino.append(nodo.direccion)
  siguienteNodo = nodo.padre
  while siguienteNodo.padre != 'N':
    camino.append(siguienteNodo.direccion)
    siguienteNodo = siguienteNodo.padre
  camino = camino[::-1]
  return camino

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

def moverJugador(movimiento, jugadorPos, cajasPos):
                  #UP,     DONW,   LEFT,    RIGHT
  #movimientos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  switcher = {
    'R': [jugadorPos[0],jugadorPos[1]+1],
    'L': [jugadorPos[0],jugadorPos[1]-1],
    'U': [jugadorPos[0]-1,jugadorPos[1]],
    'D': [jugadorPos[0]+1,jugadorPos[1]]
  }
  nuevaPos = switcher.get(movimiento,"NO")
  return nuevaPos

def moverCaja(move, caja):
  nuevaPosCaja = [move[0] + caja[0], move[1] + caja[1]]
  return nuevaPosCaja

def cajaContraPared(movimiento, nuevaPos, cajasPos, mapa):
  pared = False
  for caja in cajasPos:
    if nuevaPos == caja:
      posiblePared = moverCaja(movimiento, caja)
      if mapa[posiblePared[0]][posiblePared[1]] == 'W':
        pared = True
      else:
        pared
  return pared