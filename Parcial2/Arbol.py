from Nodo import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar_nodo(self, tipo, contenido):
        # Inserta un nodo al final
        nuevo_nodo = Nodo(tipo, contenido)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        actual = self.raiz
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_nodo(self, valor):
        # Elimina un nodo por su valor
        dummy = Nodo(0, None)
        dummy.siguiente = self.raiz
        anterior = dummy
        actual = self.raiz

        while actual:
            if actual.tipo == 0 and actual.contenido == valor:
                anterior.siguiente = actual.siguiente
                break
            anterior = actual
            actual = actual.siguiente

        self.raiz = dummy.siguiente

    def imprimir_arbol(self):
        # Imprime el árbol de manera recursiva
        def _imprimir(nodo):
            print("(", end="")
            actual = nodo
            while actual:
                if actual.tipo == 0:
                    print(actual.contenido, end="")
                else:
                    _imprimir(actual.contenido)
                if actual.siguiente:
                    print(", ", end="")
                actual = actual.siguiente
            print(")", end="")

        if self.raiz:
            _imprimir(self.raiz)
        else:
            print("()")
