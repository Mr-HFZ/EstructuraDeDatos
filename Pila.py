from ListaSimple import Nodo
from pila import Pila  

class Cola:
    def __init__(self) -> bool:
        self.cab = None
        self.fin = None
    
    def estavacia(self) -> None:
        return self.cab == None
    
    def mostrarCola(self) -> None:
        aux = self.cab
        print("Frente", end=", ")
        while aux != None:
            print(aux.valor, end=", ")
            aux = aux.sig
        print("Cola")
    
    def encolar(self, valor) -> None:
        nodo = Nodo(valor)
        if self.estavacia():
            self.cab = nodo
            self.fin = nodo
        else:
            self.fin.sig = nodo
            self.fin = nodo
    
    def desencolar(self) -> None:
        if self.estavacia():
            return None
        eliminado = self.cab
        
        if self.cab == self.fin:
            self.cab = None
            self.fin = None
        else:
            self.cab = self.cab.sig
        
        eliminado.sig = None    
        return eliminado.valor
    
    def mostrarFrente(self) -> None:
        if self.estavacia():
            return None
        return self.cab.valor
    
    def mostrarFin(self) -> None:
        if self.estavacia():
            return None
        return self.fin.valor

    # Método para construir una pila desde la cola
    def construir_pila_desde_cola(self) -> Pila:
        pila = Pila()  # Creamos una nueva pila
        while not self.estavacia():  # Mientras la cola no esté vacía
            valor = self.desencolar()  # Desencolamos un elemento
            pila.apilar(valor)  # Apilamos el elemento en la pila
        return pila
