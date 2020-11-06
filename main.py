from readMap import *
from BFS import * 
from Functions import *

if __name__ == '__main__':

    jugadorPos, cajasPos, mapa, metas = leerMapa()
    print(jugadorPos, cajasPos, mapa, metas)
    nodoRaiz = Node(jugadorPos, cajasPos, 'N', 'N',  0, mapa, metas)

    caminoBFS = busquedaPorAnchura(nodoRaiz)
    #caminoDFS = busquedaPorProfundidad(nodoRaiz)
    #caminoIDFS = busquedaPorProfunidadIterativa(nodoRaiz)
    #def __init__(self, jugadorPos, cajasPos, direccion, padre, profundidad):
    print(caminoBFS)
    

