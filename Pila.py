from ListaSimple import Nodo
class Pila:
    def __init__(self) -> None:
        self.cab = None
        self.fin = None
        
    def estavacia(self) -> bool:
        return self.cab == None
        
    def apilar(self, valor) -> None:
        nodo = Nodo(valor)
        if self.estavacia():
            self.cab = nodo
            self.fin = nodo
        else:
            nodo.sig = self.cab
            self.cab = nodo
    
    # def desapilar(self) -> None:
    #     if self.estavacia():
    #         print("La pila está vacía")
    #     else:
    #         aux = self.cab
            
    def tope(self) -> None:
        return self.cab.valor
    
    def desapilar(self)->None:
        if self.estavacia():
            return None
        eliminado=self.cab
        
        if self.cab == self.fin:
            self.cab=None
            self.fin=None
        else:
            self.cab=self.cab.sig
        
        eliminado.sig = None
        return eliminado
        
    
    #mostrar pila no es una funcion oficial
    def mostrarPila(self) -> None:
        aux = self.cab
        print("Tope")
        while aux != None:
            print(aux.valor)
            aux = aux.sig
            