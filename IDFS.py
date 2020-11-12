##Implementación algoritmo de Profundidad iterativa##
from Functions import *

def busquedaPorProfunidadIterativa(node):
        while(node):
            nodo = node[0]
            del node[0]

            if victoria(nodo.metas, nodo.cajasPos):
                return(camino(nodo))
            if nodo.profundidad <= 64:
                nuevosNodos = expandir(nodo)
                for nodo in nuevosNodos:
                    node.insert(0, nodo)