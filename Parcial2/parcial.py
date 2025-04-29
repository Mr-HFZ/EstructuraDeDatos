class Nodo:
    # Nodo de un árbol binario.
    # :param dato: Valor almacenado en el nodo.
    def __init__(self, dato):
        self.dato = dato        # Valor almacenado en el nodo
        self.izq = None         # Hijo izquierdo
        self.der = None         # Hijo derecho

# Recorrido Inorden: Izquierda - Raíz - Derecha
def recorrido_inorden(raiz):
    # Realiza un recorrido inorden de un árbol binario de manera iterativa.
    # :param raiz: Nodo raíz del árbol.
    
    pila = []  # Utilizamos una pila para el recorrido
    actual = raiz
    while pila or actual:
        while actual:  # Nos desplazamos hacia la izquierda
            pila.append(actual)
            actual = actual.izq
        actual = pila.pop()  # Procesamos el nodo actual
        print(actual.dato, end=' ')  # Imprimimos el valor del nodo
        actual = actual.der  # Pasamos al hijo derecho

# Recorrido Postorden: Izquierda - Derecha - Raíz
def recorrido_postorden(raiz):
    # Realiza un recorrido postorden de un árbol binario de manera iterativa.
    # :param raiz: Nodo raíz del árbol.
    
    if raiz is None:
        return
    pila1 = [raiz]  # Pila para recorrer el árbol
    pila2 = []  # Pila auxiliar para almacenar los nodos
    while pila1:
        nodo = pila1.pop()
        pila2.append(nodo)  # Almacenamos el nodo para posterior impresión
        if nodo.izq:
            pila1.append(nodo.izq)  # Agregamos el hijo izquierdo a la pila
        if nodo.der:
            pila1.append(nodo.der)  # Agregamos el hijo derecho a la pila
    while pila2:
        print(pila2.pop().dato, end=' ')  # Imprimimos los nodos en el orden postorden

# Recorrido Preorden: Raíz - Izquierda - Derecha
def recorrido_preorden(raiz):
    # Realiza un recorrido preorden de un árbol binario de manera iterativa.
    # :param raiz: Nodo raíz del árbol.
    
    if raiz is None:
        return
    pila = [raiz]  # Pila para recorrer el árbol
    while pila:
        nodo = pila.pop()
        print(nodo.dato, end=' ')  # Imprimimos el valor del nodo
        if nodo.der:
            pila.append(nodo.der)  # Agregamos el hijo derecho a la pila
        if nodo.izq:
            pila.append(nodo.izq)  # Agregamos el hijo izquierdo a la pila
