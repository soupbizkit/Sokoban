##Implementación algoritmo de búsqueda por profundidad##
from Node import Node
from Functions import *

estados = []
path = []

def busquedaPorProfundidad(node, estados, path):
    while (node):
        nodo = node[0]
        print(nodo.profundidad)
        estados.append([nodo.jugadorPos, nodo.cajasPos])
        del node[0]
        if victoria(nodo.metas, nodo.cajasPos):
            path.append(camino(nodo))
        else:
            if nodo.profundidad <= 64:
                nuevosNodos = expandir(nodo)
                for j, nuevo_nodo in enumerate(nuevosNodos):
                    if [nuevo_nodo.jugadorPos, nuevo_nodo.cajasPos] not in estados:
                        node.insert(j, nuevo_nodo)

                busquedaPorProfundidad(node, estados, path)

    if len(path) == 0:
        return path
    else:
        return path[0]