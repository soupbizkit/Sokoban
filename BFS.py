##Implementación algoritmo de búsqueda por anchura##
from Node import Node
from Functions import *

def busquedaPorAnchura(nodos):
    while(nodos):
        nodo = nodos[0]
        del nodos[0]

        if victoria(nodo.metas, nodo.cajasPos):
          return camino(nodo)
          
        if ciclos(nodo):
          continue
        if nodo.profundidad <= 64:
          listaMovimientos = percepcion(nodo.jugadorPos, nodo.mapa, nodo.cajasPos,nodo.metas) ##['D','L', 'R']
          
          for move in listaMovimientos:
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
            
            nuevoNodo = Node(nuevaPosJugador, listaCajas , move,
            nodo, nodo.profundidad + 1, nodo.mapa, nodo.metas)

            nodos.append(nuevoNodo)
