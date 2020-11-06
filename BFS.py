##Implementación algoritmo de búsqueda por anchura##
from Node import Node
from Functions import *

def busquedaPorAnchura(nodoRaiz):
    listaNodos = []
    resultado = ""
    if listaNodos == []:
      listaNodos.append(nodoRaiz)
    for nodoActual in listaNodos:
      print("------------------------------------")
      if nodoActual.profundidad == 64:
        resultado = "profundidad máxima alcanzada"
        break
      if victoria(nodoActual.metas, nodoActual.cajasPos):
        print("movimiento:", nodoActual.direccion)
        print("jugadorPos:", nodoActual.jugadorPos)
        print("cajasPos:", nodoActual.cajasPos)
        print("profundidad:", nodoActual.profundidad)
        resultado = camino(nodoActual)
        break

      
      listaMovimientos = percepcion(nodoActual.jugadorPos, nodoActual.mapa, nodoActual.cajasPos,nodoActual.metas) ##['D','L', 'R']

      for move in listaMovimientos:
        print("- - - - - - ")

        nuevaPosJugador = moverJugador(move, nodoActual.jugadorPos, nodoActual.cajasPos)
        listaCajas = []
        for caja in nodoActual.cajasPos:
          if nuevaPosJugador == caja:
            if move == 'R':
              movimiento = [0,1]
            if move == 'L':
              movimiento = [0,-1]
            if move == 'D':
              movimiento = [1,0]
            if move == 'U':
              movimiento = [-1,0]
            #print("estoy encima de una caja")
            nuevaPosCaja = moverCaja(movimiento, caja) 
            listaCajas.append(nuevaPosCaja)

          else:
            listaCajas.append(caja)
        
        if nodoActual == nodoRaiz:
          nuevoNodo = Node(nuevaPosJugador, listaCajas , move,
          nodoActual, 1, nodoActual.mapa, nodoActual.metas)

        else:
          nuevoNodo = Node(nuevaPosJugador, listaCajas, move, nodoActual, nodoActual.padre.profundidad + 1, nodoActual.mapa, nodoActual.metas)
        
        
        listaNodos.append(nuevoNodo)
        print("movimiento:", move)
        print("jugadorPos:", nuevoNodo.jugadorPos)
        print("cajasPos:", nuevoNodo.cajasPos)
        print("profundidad:", nuevoNodo.profundidad)    
    return resultado
        #print("direccion padre:", nodoActual.direccion)
        


