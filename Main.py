from ListaSimple import listaSimple
from ListaDoble import listaDoble
from Pila import Pila

def menu():
    print("\nSelecciona una opción:")
    print("1. Agregar elementos a la lista doblemente ligada")
    print("2. Mostrar lista doblemente ligada")
    print("3. Buscar valor en lista doblemente ligada")
    print("4. Agregar elementos desde un arreglo a la lista doblemente ligada")
    print("5. Agregar en una posición específica en la lista doblemente ligada")
    print("6. Eliminar todos los elementos de valor específico de la lista simple")
    print("7. Mostrar lista simple")
    print("8. Agregar lista simple a lista doblemente ligada")
    print("9. Agregar elementos desde la pila a la lista doblemente ligada")
    print("10. Mostrar pila")
    print("11. Salir")

def ejecutar_menu():
    lista = listaDoble()
    lista2 = listaSimple()
    pila = Pila()
    
    while True:
        menu()
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            # Agregar elementos a la lista doblemente ligada
            valor = int(input("Ingresa el valor a agregar: "))
            lista.agregar_al_final(valor)
        
        elif opcion == 2:
            # Mostrar lista doblemente ligada
            print("Lista doblemente ligada:")
            lista.mostrar_lista_izquierda_derecha()
        
        elif opcion == 3:
            # Buscar valor en la lista doblemente ligada
            valor = int(input("Ingresa el valor a buscar: "))
            encontrado = lista.buscar_valor(valor)
            if encontrado:
                print(f"El valor {valor} se encuentra en la lista.")
            else:
                print(f"El valor {valor} NO se encuentra en la lista.")
        
        elif opcion == 4:
            # Agregar elementos desde un arreglo a la lista doblemente ligada
            arreglo = list(map(int, input("Ingresa los valores del arreglo separados por espacio: ").split()))
            lista.agregar_desde_arreglo(arreglo)
        
        elif opcion == 5:
            # Agregar en una posición específica en la lista doblemente ligada
            posicion = int(input("Ingresa la posición en la que agregar el valor: "))
            valor = int(input("Ingresa el valor a agregar: "))
            lista.agregar_en_posicion(posicion, valor)
        
        elif opcion == 6:
            # Eliminar todos los elementos de valor específico en la lista simple
            valor = int(input("Ingresa el valor a eliminar de la lista simple: "))
            lista2.eliminar_todos(lista2, valor)
        
        elif opcion == 7:
            # Mostrar lista simple
            print("Lista simple:")
            lista2.mostrar_lista()
        
        elif opcion == 8:
            # Agregar lista simple a lista doblemente ligada
            lista.agregar_desde_lista_simple(lista2)
        
        elif opcion == 9:
            # Agregar elementos desde la pila a la lista doblemente ligada
            pila.apilar(10)
            pila.apilar(20)
            pila.apilar(30)
            lista.agregar_desde_pila(pila)
        
        elif opcion == 10:
            # Mostrar pila
            print("Pila:")
            pila.mostrarPila()
        
        elif opcion == 11:
            # Salir del programa
            print("Saliendo...")
            break

        else:
            print("Opción no válida, por favor selecciona otra opción.")

# Ejecución del menú interactivo
if __name__ == "__main__":
    ejecutar_menu()
