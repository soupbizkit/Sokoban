class Node:
    def __init__(self, jugadorPos, cajasPos, direccion, padre, profundidad):
        self.jugadorPos = jugadorPos
        self.cajasPos = cajasPos
        self.direccion = direccion
        self.padre = padre
        self.profundidad = profundidad
    
