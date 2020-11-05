from readMap import *
from BFS import * 
from Functions import *

if __name__ == '__main__':

    jugadorPos, cajasPos, mapa, metas = leerMapa()
    #caminoBFS = busquedaPorAnchura(nodoRaiz)
    #caminoDFS = busquedaPorProfundidad(nodoRaiz)
    #caminoIDFS = busquedaPorProfunidadIterativa(nodoRaiz)
    #def __init__(self, jugadorPos, cajasPos, direccion, padre, profundidad):
    nodoRaiz = Node(jugadorPos, cajasPos, 'N', 'N',  0, mapa)
    print(nodoRaiz.jugadorPos)
    print(jugadorPos, cajasPos, mapa, metas)

