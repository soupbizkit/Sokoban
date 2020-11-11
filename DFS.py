##Implementación algoritmo de búsqueda por profundidad##
from Node import Node
from Functions import *

def busquedaPorProfundidad(node):
    while(node):
        nodo = node[0]
        del node[0]

        if victoria(nodo.metas, nodo.cajasPos):
            return(camino(nodo))
        if nodo.profundidad <= 64:
            nuevosNodos = expandir(nodo)
            for nodo in nuevosNodos:
                node.insert(0, nodo)