
from Nodo import Nodo
class listaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self)->bool: 
        return self.cabeza is None

    def agregar_al_inicio(self, valor): 
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def mostrar_lista_izquierda_derecha(self): 
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" <->")
            actual = actual.siguiente
        print('nulo')

    def agregar_en_posicion(self, posicion, valor):
        if posicion == 0:
            self.agregar_al_inicio(valor)
            return
        
        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        
        indice = 0

        while actual is not None and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1

        if actual is None:
            self.agregar_al_final(valor)
        else:
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    

    def eliminar_del_inicio(self): 
        if self.esta_vacia():
            return False
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        return True

    def eliminar_del_final(self)-> bool: 
       if self.esta_vacia():  
        return False

       if self.cabeza == self.cola: 
            self.cabeza = self.cola = None
       else:
        self.cola = self.cola.anterior  
        self.cola.siguiente = None  
        return True
        
        
    def eliminar_de_posicion(self, posicion: int) -> bool: 
    
        if self.esta_vacia() or posicion < 0:
            return False

        if posicion == 0:
            return self.eliminar_del_inicio()  

        actual = self.cabeza
        contador = 0

   
        while actual is not None and contador < posicion: 
             actual = actual.siguiente
             contador += 1

        if actual is None:  
            return False

    
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior

    
        if actual == self.cola:
            self.cola = actual.anterior

        return True
    
    def eliminar_valor(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                if actual == self.cola:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def buscar_valor(self, valor)->bool: 
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def buscar_nodo(self, valor) : 
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return id(actual) 
            actual = actual.siguiente
            
        return None
    
    def agregar_desde_arreglo(self, arreglo):  
        for valor in arreglo:
            self.agregar_al_final(valor)

    def agregar_al_final(self, valor): 
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def agregar_desde_lista_simple(self, lista_simple):
        nodo_actual = lista_simple.cabeza
        while nodo_actual:
            self.agregar_al_final(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
            
    def agregar_desde_pila(self, pila_simple):
        nodo_actual = pila_simple.cab
        while nodo_actual:
            self.agregar_al_final(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente



