##Implementación algoritmo de búsqueda por anchura##
from Node import Node
from Functions import *

def busquedaPorAnchura(nodos):
    while(nodos):
        nodo = nodos[0]
        del nodos[0]

        if victoria(nodo.metas, nodo.cajasPos):
          return camino(nodo)
 
        if nodo.profundidad <= 64:
          listaNodos = expandir(nodo)
          for nodo in listaNodos:
              nodos.append(nodo)


            
