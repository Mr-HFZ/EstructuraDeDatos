#Ppal
from ListaSimple import listaSimple
from ListaDoble import listaDoble
from Pila import Pila

lista=listaDoble()

lista.agregar_al_final(8)
lista.agregar_al_final(10)
lista.agregar_al_final(20)
vector=[1,2,3,4,5]
lista.agregar_desde_arreglo(vector)
lista.agregar_en_posicion(3,100)
lista.mostrar_lista_izquierda_derecha()
busqueda=lista.buscar_valor(100)
# print(f'El valor 100 se encuentra en la lista?: {busqueda}')

lista2=listaSimple()
lista2.agregar_al_final(10)
lista2.agregar_al_final(20)
lista2.agregar_al_final(30)
lista2.mostrar_lista()

lista.agregar_desde_lista_simple(lista2)
pila=Pila()
pila.apilar(200)
pila.apilar(300)
pila.apilar(400)
lista.agregar_desde_pila(pila)

lista.mostrar_lista_izquierda_derecha()