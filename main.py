from readMap import *
from BFS import * 
from Functions import *
from DFS import *
from IDFS import *
import sys

if __name__ == '__main__':


    print(sys.argv[1])

    jugadorPos, cajasPos, mapa, metas = leerMapa()
    nodoRaiz = Node(jugadorPos, cajasPos, 'N', 'N',  0, mapa, metas)
    nodos = []
    nodos.append(nodoRaiz)

    if(sys.argv[1] == "BFS"):
        caminoBFS = busquedaPorAnchura(nodos)
        print("camino BFS", caminoBFS)
    if(sys.argv[1] == "DFS"):
        print("jugador:",jugadorPos)
        print("cajas:",cajasPos)
        print("metas:",metas)
        caminoDFS = busquedaPorProfundidad(nodos, [], [])
        print("camino DFS",caminoDFS)
    if(sys.argv[1] == "IDFS"):
        caminoIDFS = busquedaPorProfunidadIterativa(nodos)
        print("camino IDFS", caminoIDFS)
    
    
    
    
    

