from Arbol import Arbol
from Nodo import Nodo

# Crear una estructura principal de tipo Árbol
estructura = Arbol()

# Insertar un dato simple "A"
estructura.insertar_nodo(0, "A")

# Crear una subestructura: B -> C
nodo_b = Nodo(0, "B")
nodo_c = Nodo(0, "C")
nodo_b.siguiente = nodo_c  # Unir B con C
subestructura = Nodo(1, nodo_b)  # Nodo de tipo subestructura (tipo = 1)

# Insertar la subestructura dentro del árbol
estructura.insertar_nodo(1, subestructura.contenido)

# Insertar otro dato simple "D"
estructura.insertar_nodo(0, "D")

# Imprimir el árbol actual
estructura.imprimir_arbol()
print()  # salto de línea

# Insertar un dato adicional "E"
estructura.insertar_nodo(0, "E")

# Imprimir el árbol actualizado
estructura.imprimir_arbol()
print()

# Eliminar el dato "D"
estructura.eliminar_nodo("D")

# Imprimir el árbol después de eliminar
estructura.imprimir_arbol()
print()
