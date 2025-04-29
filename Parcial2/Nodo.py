class Nodo:
    # Nodo de una estructura de datos enlazada o árbol.
    # :param tipo: 0 si es un dato simple, 1 si es una subestructura.
    # :param contenido: Dato o referencia a otro Nodo.
    
    def __init__(self, tipo, contenido):
        self.tipo = tipo          # 0 = dato, 1 = subestructura
        self.contenido = contenido  # Puede ser un dato o referencia a otro nodo
        self.siguiente = None     # Enlace al siguiente nodo
