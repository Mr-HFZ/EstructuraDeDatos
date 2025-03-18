class Pila:
    def __init__(self, cantidad):
        self.datos = []
        self.top = -1
        self.cantidad = cantidad

    def adiciona(self, dato):
        if self.top < self.cantidad - 1:
            self.top += 1
            self.datos.append(dato)
        else:
            print("La pila está llena. No se puede agregar más elementos.")

    def sacar(self):
        if self.top >= 0:
            self.datos.pop(self.top) 
            self.top -= 1
        else:
            print("La pila está vacía. No se puede sacar elementos.")

    def visualizar(self):
        print("Pila:", self.datos)

    def verTop(self):
        if self.top >= 0:
            print(f"Elemento en la cima: {self.datos[self.top]} (índice {self.top})")
        else:
            print("La pila está vacía.")

# Código principal
num = int(input("Digite el tamaño de la pila:\n"))
pilas = Pila(num)

# Insertar datos
for i in range(num):
    pilas.adiciona(input(f"Inserte dato {i + 1}: "))

pilas.visualizar()

# Sacar elementos
c = input("Para sacar un elemento, digite un número diferente a 0:\n")
if int(c) != 0:
    pilas.sacar()

pilas.visualizar()
