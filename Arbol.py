class ArbolGeneral:
    def __init__(self, raiz_valor=None):
        if raiz_valor is not None:
            self.raiz = Nodo(raiz_valor)
        else:
            self.raiz = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def agregar_hijo(self, valor_padre, valor_hijo) -> bool:
        """
        Busca el nodo con valor valor_padre y agrega un hijo con valor valor_hijo.
        Retorna True si se agregó, False si no encontró el nodo padre.
        """
        if self.raiz is None:
            return False
        nodo_padre = self._buscar_nodo(self.raiz, valor_padre)
        if nodo_padre:
            nuevo_hijo = Nodo(valor_hijo)
            nodo_padre.hijos.append(nuevo_hijo)
            return True
        return False

    def _buscar_nodo(self, nodo_actual, valor):
        """
        Busca recursivamente el nodo con el valor dado.
        """
        if nodo_actual.valor == valor:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            resultado = self._buscar_nodo(hijo, valor)
            if resultado:
                return resultado
        return None

    def mostrar_arbol(self, nodo=None, nivel=0):
        """
        Muestra el árbol de manera jerárquica.
        """
        if self.raiz is None:
            print("Árbol vacío")
            return
        if nodo is None:
            nodo = self.raiz
        print("    " * nivel + str(nodo.valor))
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)

    def eliminar_hijo(self, valor_padre, valor_hijo) -> bool:
        """
        Elimina el hijo con valor valor_hijo del nodo con valor valor_padre.
        Retorna True si se eliminó, False si no se encontró.
        """
        nodo_padre = self._buscar_nodo(self.raiz, valor_padre)
        if nodo_padre:
            for i, hijo in enumerate(nodo_padre.hijos):
                if hijo.valor == valor_hijo:
                    nodo_padre.hijos.pop(i)
                    return True
        return False

    def buscar_valor(self, valor) -> bool:
        """
        Busca si un valor está en el árbol.
        """
        return self._buscar_nodo(self.raiz, valor) is not None

    def recorrer_preorden(self, nodo=None):
        """
        Recorrido preorden: nodo -> hijos.
        """
        if self.raiz is None:
            return
        if nodo is None:
            nodo = self.raiz
        print(nodo.valor, end=" ")
        for hijo in nodo.hijos:
            self.recorrer_preorden(hijo)

    # Puedes agregar más métodos para agregar nodos de distintas formas, eliminar subárboles, etc.
