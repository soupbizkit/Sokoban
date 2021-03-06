from Node import *

def percepcion(jugadorPos, mapa, cajasPos, metas):
                    #UP,     DONW,   LEFT,    RIGHT
    movimientos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    movesResult = []

    for i in movimientos:
      nuevaPos =[jugadorPos[0] + i[0], jugadorPos[1] + i[1]] #encuentra la nueva posicion del jugador

      if cajaCercana(i, nuevaPos, cajasPos): #Verifica si hay 2 cajas en fila hacia esa dirección
        continue

      if cajaContraPared(i, nuevaPos, cajasPos, mapa): #Verifica si al mover una caja en una dirección hay una pared
        continue

      if cajaEnEsquina(i, nuevaPos, cajasPos, metas,mapa): #Verifica si la caja quedará en una esquina
        continue

      if mapa[nuevaPos[0]][nuevaPos[1]] == 'W': #si la nueva posición es una pared
        continue
        
      elif i == [-1, 0]:
        movesResult.append('U')
      elif i == [1, 0]:
        movesResult.append('D')
      elif i == [0, -1]:
        movesResult.append('L')
      elif i == [0, 1]:
        movesResult.append('R')

    return movesResult

#expande un nodo basandose en sus percepciones
def expandir(nodo):
  nodos = []
  listaMovimientos = percepcion(nodo.jugadorPos, nodo.mapa, nodo.cajasPos, nodo.metas) 
  for move in listaMovimientos: #['R','D']
    nuevaPosJugador = moverJugador(move, nodo.jugadorPos)
    listaCajas = []
    for caja in nodo.cajasPos:
      if nuevaPosJugador == caja:
        if move == 'R':
          movimiento = [0,1]
        if move == 'L':
          movimiento = [0,-1]
        if move == 'D':
          movimiento = [1,0]
        if move == 'U':
          movimiento = [-1,0]
        nuevaPosCaja = moverCaja(movimiento, caja) 
        listaCajas.append(nuevaPosCaja)

      else:
        listaCajas.append(caja)    
    nuevoNodo = Node(nuevaPosJugador, listaCajas , move, nodo, nodo.profundidad + 1, nodo.mapa, nodo.metas)

    if ciclos(nuevoNodo):
      continue
    else:
      nodos.append(nuevoNodo)

  return nodos

#verifica si existe otra caja hacia la dirección que se va mover una caja
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


#retorna true o false si las cajas están en la posición de las metas          
def victoria(metas, cajasPos):
  metasSort = sorted(metas)
  cajasSort = sorted(cajasPos)
  if metasSort == cajasSort:
    return True
  else:
    return False

def moverJugador(movimiento, jugadorPos):
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


#retorna el camino desde un nodo dado hasta el nodo raíz
def camino(nodo):
  camino = []
  camino.append(nodo.direccion)
  siguienteNodo = nodo.padre
  while siguienteNodo != 'N':
      camino.append(siguienteNodo.direccion)
      siguienteNodo = siguienteNodo.padre
  camino = camino[::-1]
  del camino[0]
  return camino

#Verifica si hay bucles
def ciclos(nodo):
  padre = nodo.padre
  while padre != 'N':
    if nodo.jugadorPos == padre.jugadorPos and nodo.cajasPos == padre.cajasPos:
      return True
    else:
      padre = padre.padre
  return False

#cambia la posición de una caja
def moverCaja(move, caja):
  nuevaPosCaja = [move[0] + caja[0], move[1] + caja[1]]
  return nuevaPosCaja


#verifica si al mover una caja, esta va a quedar en una esquina
def cajaEnEsquina(movimiento, nuevaPos, cajaPos, metas, mapa): 
                  #UP,     DONW,   LEFT,    RIGHT
  #movimientos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  for caja in cajaPos:
    if caja == nuevaPos:
      nuevaPosCaja = [movimiento[0] + caja[0], movimiento[1] + caja[1]]

      for meta in metas:
        if nuevaPosCaja == meta:
          return False
        else:
        #esquina superior izquierda
          if mapa[nuevaPosCaja[0]][nuevaPosCaja[1]-1]=='W' and mapa[nuevaPosCaja[0]-1][nuevaPosCaja[1]]=='W':
            return True

          #esquina superior derecha
          elif mapa[nuevaPosCaja[0]][nuevaPosCaja[1]+1]=='W' and mapa[nuevaPosCaja[0]-1][nuevaPosCaja[1]]=='W':
            return True

          #esquina inferior izquierda
          elif mapa[nuevaPosCaja[0]][nuevaPosCaja[1]-1]=='W' and mapa[nuevaPosCaja[0]+1][nuevaPosCaja[1]]=='W':
            return True
          
          #esquina inferior derecha
          elif mapa[nuevaPosCaja[0]][nuevaPosCaja[1]+1]=='W' and mapa[nuevaPosCaja[0]+1][nuevaPosCaja[1]]=='W':
            return True
          else:
            return False


#Verifica si la caja que se va mover está al lado de una pared
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