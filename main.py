from readMap import *
from BFS import * 
from Functions import *
from DFS import *
from IDFS import *
import sys

if __name__ == '__main__':
    jugadorPos, cajasPos, mapa, metas = leerMapa()
    nodoRaiz = Node(jugadorPos, cajasPos, 'N', 'N',  0, mapa, metas)
    nodos = []
    nodos.append(nodoRaiz)

    if(sys.argv[1] == "BFS"):
        caminoBFS = busquedaPorAnchura(nodos)
        print("camino BFS:", caminoBFS)
    if(sys.argv[1] == "DFS"):
        caminoDFS = busquedaPorProfundidad(nodos, [], [])
        print("camino DFS:",caminoDFS)
    if(sys.argv[1] == "IDFS"):
        caminoIDFS = busquedaPorProfunidadIterativa(nodos)
        print("camino IDFS:", caminoIDFS)
    
    
    
    
    

