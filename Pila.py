from ListaSimple import Nodo  # Importamos la clase Nodo para los nodos de la pila

class Pila:
    def __init__(self) -> None:
        self.cab = None  # Apuntador al primer nodo (cima de la pila)
        self.fin = None  # Apuntador al último nodo (no necesario para la pila, pero se deja por consistencia)
        
    def estavacia(self) -> bool:
        """Verifica si la pila está vacía"""
        return self.cab == None
        
    def apilar(self, valor) -> None:
        """Agrega un elemento al tope de la pila"""
        nodo = Nodo(valor)
        if self.estavacia():
            self.cab = nodo
            self.fin = nodo
        else:
            nodo.sig = self.cab
            self.cab = nodo
    
    def tope(self) -> None:
        """Devuelve el valor del tope de la pila"""
        if self.estavacia():
            return None
        return self.cab.valor
    
    def desapilar(self) -> None:
        """Elimina el elemento en el tope de la pila"""
        if self.estavacia():
            return None
        eliminado = self.cab
        
        if self.cab == self.fin:
            self.cab = None
            self.fin = None
        else:
            self.cab = self.cab.sig
        
        eliminado.sig = None
        return eliminado
    
    def mostrarPila(self) -> None:
        """Muestra todos los elementos de la pila desde el tope hasta la base"""
        aux = self.cab
        print("Tope")
        while aux != None:
            print(aux.valor)
            aux = aux.sig
