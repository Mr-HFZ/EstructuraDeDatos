from Nodo import Nodo
from Pila import Pila
#Nodo Simple
class NodoSimple:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


#Lista Simple
class listaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("Nulo")
